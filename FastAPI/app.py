'''
The app
'''
from fastapi import FastAPI, Request,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_404_NOT_FOUND


templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/css", StaticFiles(directory="./templates/css"))
app.mount("/img", StaticFiles(directory="./templates/img"))
app.mount("/js", StaticFiles(directory="./templates/js"))
app.mount("/vendor", StaticFiles(directory="./templates/vendor"))


@app.get("/")
async def index(request: Request):
    '''
    Home page
    '''
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/{filename}")
async def read_root(filename: str, request: Request):
    try:
        return templates.TemplateResponse(f"{filename}", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"Template {filename}.html not found")

