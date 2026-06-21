from fastapi import FastAPI, Response, status, HTTPException
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


my_posts = [{"title": "Post 1", "content": "Content of post 1", "published": True, "rating": 5, "id": 1},
            {"title": "Post 2", "content": "Content of post 2", "published": False, "rating": 4, "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

# an endpoint that returns a welcome message
@app.get("/")
def root():
    return {"message":"Welcome to my API!"}


# an endpoint that returns a list of posts
@app.get("/posts")
def get_posts():
    return {"posts": my_posts}




# an endpoint that takes a post with a schema as a body parameter and returns the post created successfully
@app.post("/createPost", status_code= status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    # not using a database yet, so we will generate a random id for the post
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"Data": post.dict()}



# an endpoint that takes a path parameter and returns the post with that id
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    return {"post_detail": post}