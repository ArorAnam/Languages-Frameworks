from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import graph_traverse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/home")
async def display_website_home(request: Request):
    vertices = graph_traverse.gtraverse()

    for i in range(len(vertices)):
        if 'votes' in vertices[i]['_id']:
            python_votes = vertices[i]['votes']

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "votes": python_votes
        })


@app.post("/home/upvote_link")
async def Upvote_Link(request: Request):
    vertices = graph_traverse.gtraverse()

    for i in range(len(vertices)):
        if 'votes' in vertices[i]['_id']:
            vertices[i]['votes'] += 1
            python_votes = vertices[i]['votes']

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "votes": python_votes
        })
