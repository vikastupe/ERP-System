import uvicorn
from fastapi import FastAPI, APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse

app = FastAPI()
api_router = APIRouter()
templates = Jinja2Templates(directory="templates")




@app.get('/', RedirectResponse=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('welcome.html', {'request': request})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)

