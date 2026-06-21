from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "Post 1", "content": "Content of post 1", "published": True, "rating": 5},
            {"title": "Post 2", "content": "Content of post 2", "published": False, "rating": 4}]


# creating a root endpoint that returns a welcome message
@app.get("/")
def root():
    return {"message":"Welcome to my API!"}


# creating a posts endpoint that returns a list of posts
@app.get("/posts")
def get_posts():
    return {"posts": my_posts}



# creating a post endpoint that takes a post as a path parameter that returns a message of the post created successfully
@app.post("/create_post/{post}")
def create_post(post: str):
    return {"message": f"Post '{post}' created successfully!"}


# creating a post with a schema that takes a post as a body parameter that returns the post created successfully
@app.post("/createPost")
def create_posts(post: Post):
    post_dict = post.dict()
    # not using a database yet, so we will generate a random id for the post
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"Data": post.dict()}