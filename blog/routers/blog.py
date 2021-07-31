from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from blog.oauth2 import get_current_user
from blog.database import get_db
from blog.repository import blog
from blog.schemas import ShowBlog, Blog, User
router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/', response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.get_all(db)


@router.get('/{id}', status_code= status.HTTP_200_OK, response_model=ShowBlog)
def get_blog(id, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.get(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.create(request, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.destroy(id, db)
