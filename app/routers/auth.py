from fastapi import APIRouter, HTTPException, status, Depends, responses
from sqlalchemy.orm import Session
from .. import models, utils,database, OAuth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags= ["Authentication"]
)

@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")
    
    access_token = OAuth2.create_access_token(data={"user_id": user.id}) 
    #access_token_id_11 = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMSwiZXhwIjoxNjQ2NjQ5OTc2fQ.aDLaQkGmzqu6Dvu5QW-ywRT5NcmPxkqOzjOrTYPQsdA




    return {"Access_token": access_token, "token type": "bearer"}


