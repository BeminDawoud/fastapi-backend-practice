from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# creating a root endpoint that returns a welcome message
@app.get("/")
def root():
    return {"message":"Welcome to my API!"}


# creating a posts endpoint that returns a list of posts
@app.get("/posts")
def get_posts():
    return {"posts": ["Post 1", "Post 2", "Post 3"]}



# creating a post endpoint that takes a post as a path parameter that returns a message of the post created successfully
@app.post("/create_post/{post}")
def create_post(post: str):
    return {"message": f"Post '{post}' created successfully!"}


# creating a post with a schema that takes a post as a body parameter that returns the post created successfully
@app.post("/createPost")
def create_posts(post: Post):
    print(post.title)
    return {"Data": post.dict()}