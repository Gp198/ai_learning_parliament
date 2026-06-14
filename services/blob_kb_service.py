import os
from dataclasses import dataclass
from typing import List
from azure.storage.blob import BlobServiceClient, ContainerClient

@dataclass
class KBDocument:
    name: str
    content: str

def _container_client() -> ContainerClient:
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER") or os.getenv("AZURE_STORAGE_CONTAINER_PUBLIC", "ai-learning-parliament")

    if connection_string:
        service = BlobServiceClient.from_connection_string(connection_string)
        return service.get_container_client(container_name)

    account_url = os.getenv("AZURE_STORAGE_ACCOUNT_URL")
    if not account_url:
        raise ValueError("Missing Azure Storage config. Set AZURE_STORAGE_CONNECTION_STRING or AZURE_STORAGE_ACCOUNT_URL.")
    return ContainerClient(account_url=account_url, container_name=container_name)

def load_kb_documents() -> List[KBDocument]:
    container = _container_client()
    docs: List[KBDocument] = []

    for blob in container.list_blobs():
        if not (blob.name.endswith(".md") or blob.name.endswith(".json") or blob.name.endswith(".txt")):
            continue
        raw = container.download_blob(blob.name).readall()
        content = raw.decode("utf-8", errors="ignore")
        docs.append(KBDocument(name=blob.name.split("/")[-1], content=content))

    return docs

def load_kb(max_chars: int | None = None) -> str:
    max_chars = max_chars or int(os.getenv("KB_MAX_CHARS", "45000"))
    docs = load_kb_documents()
    chunks = []
    total = 0

    for doc in docs:
        block = f"\n\nFILE: {doc.name}\n{doc.content}\n"
        if total + len(block) > max_chars:
            remaining = max_chars - total
            if remaining > 500:
                chunks.append(block[:remaining])
            break
        chunks.append(block)
        total += len(block)

    return "".join(chunks)

def list_kb_files() -> list[str]:
    return [doc.name for doc in load_kb_documents()]
