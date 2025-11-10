from fastapi import FastAPI

this_app = FastAPI()

@this_app.get("/hello-world")
def hw():
   return {"message" : "HELLO my WORLD"} 