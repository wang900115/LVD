from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash, generate_password_hash
from internal.domain.interface.user import UserInterface
from internal.adapter.sqlachemy.model.user import UserTable
from internal.domain.entities.user import User
from internal.adapter.sqlachemy.validtor.user import UserValidator

class UserImplement(UserInterface):

    def __init__(self, db: Session):
        self.db = db

    def CreateUser(self, user: User) -> User:
        existingUser = self.db.query(UserTable).filter_by(username=user.username).first()
        if existingUser:
            raise ValueError("this user have been created")
        
        validatedUser = UserValidator(**user.__dict__)

        newUser = UserTable(username=validatedUser.username,
                             password=generate_password_hash(validatedUser.password,"pbkdf2:sha256"),
                             email=validatedUser.email)
        
        self.db.add(newUser)
        self.db.commit()
        self.db.refresh(newUser)
        return newUser.Domain()
    
    def QueryUser(self, username: str)-> UserTable:
        resultUser = self.db.query(UserTable).filter_by(username=username).first()
        if resultUser is None:
            raise ValueError("username wrong")
        return resultUser
    
    def UpdateUser(self, user: User) -> User:
        resultUser = self.QueryUser(user.username)
        validatedUser = UserValidator(**user.__dict__)
        resultUser.email = validatedUser.email
        if not check_password_hash(resultUser.password, validatedUser.password):
            resultUser.password = generate_password_hash(validatedUser.password, "pbkdf2:sha256")
        self.db.commit()
        self.db.refresh(resultUser)
        return resultUser.Domain()
    
    def Login(self, username: str, password: str) -> User:
        resultUser = self.QueryUser(username)
        if not check_password_hash(resultUser.password, password):
            raise ValueError("password wrong")
        return resultUser.Domain()
    


        


        