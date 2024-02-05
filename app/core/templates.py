from fastapi.templating import Jinja2Templates

from core.paths import setup_path

templates = Jinja2Templates(directory=setup_path("templates"))
