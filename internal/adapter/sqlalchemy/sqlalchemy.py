from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Mysql:

    def __init__(self, config: dict):
        self.host = config.get("host","localhost")
        self.port = config.get("port", 3306)
        self.user = config.get("user","root")
        self.password = config.get("password","")
        self.database = config.get("name","")

    def Session(self):
        url = f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        engine = create_engine(url, pool_size=5)
        return sessionmaker(bind=engine)