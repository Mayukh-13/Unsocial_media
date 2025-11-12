from pydantic import BaseModel
class PostCreate(BaseModel):
    title : str
    Desc: str