from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from blog import schemas
from blog.database import get_db
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return user.get_user(id, db)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)
