from fastapi import FastAPI, HTTPException

this_app = FastAPI()

text_posts = {
    1: {"title": "First Post", "Desc": "Gud yaar"},
    2: {"title": "Second Post", "Desc": "Bhai scene on hai"},
    3: {"title": "Third Post", "Desc": "Kal milte hai"},
    4: {"title": "Fourth Post", "Desc": "Coding vibes"},
    5: {"title": "Fifth Post", "Desc": "Aaj mood mast"},
    6: {"title": "Sixth Post", "Desc": "Life set"},
    7: {"title": "Seventh Post", "Desc": "Kya bolti public"},
    8: {"title": "Eighth Post", "Desc": "Chai break"},
    9: {"title": "Ninth Post", "Desc": "Thoda kaam karo"},
    10: {"title": "Tenth Post", "Desc": "Sona zaroori hai"},
}


@this_app.get("/posts")# ? -> denotes the query parameters
def get_all_posts(lim : int):
   if lim:
      return list(text_posts.values())[:lim]


# Get operation with custom path parameter 
@this_app.get("/posts/{id}")
def get_post(id: int):
   if id not in text_posts:
      raise HTTPException(status_code=403, detail=  "Post not found!!!!")
   return text_posts.get(id)