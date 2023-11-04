from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str

class PostInDB(Post):
    id: int