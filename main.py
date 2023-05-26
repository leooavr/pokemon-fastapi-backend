from fastapi import FastAPI
import uvicorn
from routes.trainer import trainer
from routes.pokemon import pokemon

app = FastAPI(title="Pokemon Api", version='0.1.1', description="Esta es la documentación de la API Pokemon elaborada con FastAPI utilizando MongoDB")

app.include_router(trainer)
app.include_router(pokemon)



if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
