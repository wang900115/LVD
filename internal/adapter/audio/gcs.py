from google.cloud import storage
from typing import BinaryIO

BUCKET_NAME = "LVD"


# def downloadAudioStream(blobName: str) -> BinaryIO:
#     client = storage.Client()
#     bucket = client.bucket(BUCKET_NAME)
#     blob = bucket.blob(blobName)
#     return blob.open("rb")


class GCS:

    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.bucket("LVD")

    def Upload(self, file: bytes, filename: str, type: str) -> None:
        blob = self.bucket.blob(filename)
        blob.upload_from_file(file, content_type=type)
        
    def Download(self, blobName: str) -> BinaryIO:
        return self.bucket.blob(blobName).open("rb")

    def Delete(self, blobName: str) -> None:
        blob = self.bucket.blob(blobName)
        if not blob.exists():
            raise FileNotFoundError(
                f"Blob '{blobName}' not found in bucket '{BUCKET_NAME}'")
        blob.delete
