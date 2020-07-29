from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import update_db_record
import graph_traverse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_vertices():
    return graph_traverse.gtraverse('lang1')


@app.get("/home")
async def display_website_home(request: Request):
    vertices = get_vertices()

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "lang1_name": vertices['name'],
            "votes1": vertices['votes1'],
            "votes2": vertices['votes2'],
            "votes3": vertices['votes3']
        })


@app.post("/home/cdc")
async def Upvote_Link(request: Request):
    update_db_record.update_votes_cdc(get_vertices()['votes1'] + 1, 'course_depth_coverage')
    vertices = get_vertices()

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "lang1_name": vertices['name'],
            "votes1": vertices['votes1'],
            "votes2": vertices['votes2'],
            "votes3": vertices['votes3']
        })


@app.post("/home/cwe")
async def Upvote_Link(request: Request):
    update_db_record.update_votes_cwe(get_vertices()['votes2'] + 1, 'concepts_well_explained')
    vertices = graph_traverse.gtraverse('lang1')

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "lang1_name": vertices['name'],
            "votes1": vertices['votes1'],
            "votes2": vertices['votes2'],
            "votes3": vertices['votes3']
        })


@app.post("/home/qoc")
async def Upvote_Link(request: Request):
    update_db_record.update_votes_qoc(get_vertices()['votes3'] + 1, 'quality_of_content')
    vertices = graph_traverse.gtraverse('lang1')

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "lang1_name": vertices['name'],
            "votes1": vertices['votes1'],
            "votes2": vertices['votes2'],
            "votes3": vertices['votes3']
        })
