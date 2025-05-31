from google.cloud import storage
from typing import BinaryIO

BUCKET_NAME = "LVD"


def downloadAudioStream(blobName: str) -> BinaryIO:
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(blobName)
    return blob.open("rb")