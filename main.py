from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import HTMLResponse, FileResponse
from routes.trainer import trainer
from routes.pokemon import pokemon

app = FastAPI(title="Pokemon Api", version='0.1.1',
              description="Esta es la documentación de la API Pokemon elaborada con FastAPI utilizando MongoDB")
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", response_class=HTMLResponse)
async def root():
    html_route = "./views/login.html"
    return FileResponse(html_route, status_code=200)


app.include_router(trainer)
app.include_router(pokemon)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
