import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# MariaDB 연동작업
# 데이터 베이스 이름://계정이름:비밀번호@localhost:3306/저장하려는 데이터베이스(테이블이 아니다.)
DATABASEURL = "mariadb+pymysql://root:1234@localhost:3306/FEMS"

engine = sqlalchemy.create_engine(DATABASEURL, encoding = "utf-8")

SeeionLocal = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.ext.declarative.declarative_base()

