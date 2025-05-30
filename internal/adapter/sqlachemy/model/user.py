from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from internal.domain.entities.user import User

Base = declarative_base()

class UserTable(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String, nullable=False)

    def Domain(self):
        return User(
            username=self.username
        )