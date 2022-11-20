# main은 프론트엔드와 소통할 api 생성하는 곳 ,, 작동은 services에서
from typing import List
import fastapi
import fastapi.security

import sqlalchemy.orm

import services
import schemas

app = fastapi.FastAPI()


# 실행 구문 : uvicorn main:app --reload
# 화면에서 local주소 뒤에 /docs 입력 후 작업

# Token를 부여할 ID와 Password 지정 // 이 기능 필요없음
@app.post("/api/users")
async def create_user(user: schemas.UserCreate, db: sqlalchemy.orm.Session = fastapi.Depends(services.get_db)):
    db_user = await services.get_user_by_ID(user.LoginID, db)
    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="ID already in use") # 아이디 있는지없는지 확인이라 없어도 되는 기능
    
    user = await services.create_user(user, db)
    
    return await services.create_token(user)

# ID password 확인 후 Token 부여하기 , user(ID, Password)가 없으면 부여하지 못한다.  , 이기능이 핵심
# 메인페이지로 토큰들고 넘어가게 , form_data에서 id와 비번을 가져올수 있다.
@app.post("/api/token")
async def generate_token(form_data : fastapi.security.OAuth2PasswordRequestForm = fastapi.Depends(), db: sqlalchemy.orm.Session = fastapi.Depends(services.get_db)):
    user = await services.authenticate_user(form_data.username, form_data.password, db)
    
    # 없는 아이디면 뜨는 경고
    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    
    return await services.create_token(user)

# 부여받은 ID 보여주기 , main page 로 넘어가게,, 아마 다른 페이지 이동할 때도 유사하게 사용 예정
@app.get("/api/users/main", response_model=schemas.User)
async def get_user(user: schemas.User = fastapi.Depends(services.get_current_user)):
    return user