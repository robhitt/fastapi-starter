from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root_api():
  return {
    "message": "Welcome to Rob's Blog"
  }