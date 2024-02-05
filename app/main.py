import datetime

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

from core import templates
from core.paths import setup_path

app = FastAPI()
app.mount("/static", StaticFiles(directory=setup_path("static")), name="static")


items = [
    {"id": i, "hehe": "bebe", "title": f"Title {i}", "content": "asdasdasdasdasdasdad" * 100, "created": datetime.datetime.now(tz=datetime.timezone.utc)} for i in range(1, 6)
]  # just developing mock


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items": items})
