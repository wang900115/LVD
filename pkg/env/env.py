from dotenv import load_dotenv
import os 

class EnvConfig:

    def __init__(self, path: str):
        load_dotenv(path)

        self.BUCKET_NAME: str = os.getenv("BUCKET_NAME", "default-bucket")
        self.BASE_SECRET: str = os.getenv("BASE_SECRET", "default-secret")
    