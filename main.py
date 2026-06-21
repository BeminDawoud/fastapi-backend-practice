from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Welcome to my API!"}


@app.get("/posts")
def get_posts():
    return {"posts": ["Post 1", "Post 2", "Post 3"]}


@app.post("/create_post/{post}")
def create_post(post: str):
    return {"message": f"Post '{post}' created successfully!"}