import sqlalchemy
import sqlalchemy.orm
import passlib.hash

import database

# 테이블 정의
# 이러면 지정했던 데이터 베이스(FEMS)에 User테이블이 생성하기 위한 구조
# 우리는 User 계정 하나만 있으면 된다.
class User(database.Base):
    __tablename__ = "LoginID"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    LoginID = sqlalchemy.Column(sqlalchemy.String(255), unique=True, index=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String(255), index=True)
    
    def verify_password(self, password:str):
        return passlib.hash.bcrypt.verify(password, self.hashed_password)
    
    