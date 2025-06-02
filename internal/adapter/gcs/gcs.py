from google.cloud import storage
from google.oauth2 import service_account
from typing import BinaryIO

# def downloadAudioStream(blobName: str) -> BinaryIO:
#     client = storage.Client()
#     bucket = client.bucket(BUCKET_NAME)
#     blob = bucket.blob(blobName)
#     return blob.open("rb")


class GCS:

    def __init__(self, buckName: str):
        self.client = storage.Client(credentials=service_account.Credentials.from_service_account_file("C:\\Users\\a0970\\2025\\2025 04-06\\LVD\\config\\angelic-hold-461004-k3-116c6af34d65.json"), project="803")
        self.bucket = self.client.bucket(buckName)

    def Upload(self, file: bytes, filename: str, type: str) -> None:
        blob = self.bucket.blob(filename)
        blob.upload_from_file(file, content_type=type)
        
    def Download(self, blobName: str) -> BinaryIO:
        return self.bucket.blob(blobName).open("rb")

    def Delete(self, blobName: str) -> None:
        blob = self.bucket.blob(blobName)
        if not blob.exists():
            raise FileNotFoundError(
                f"Blob '{blobName}' not found in bucket '{self.bucket}'")
        blob.delete
