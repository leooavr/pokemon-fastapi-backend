from fastapi import APIRouter, HTTPException
from models.trainer import Trainer
from database.trainer import (
    get_all_trainers,
    get_one_trainer,
    create_trainer,
    remove_trainer,
    update_trainer
)
trainer = APIRouter()

@trainer.get('/trainers',response_model=list[Trainer], tags=['trainer'])
async def get_trainers():
    response = await get_all_trainers()
    return response

@trainer.get('/trainers/{username}', response_model=Trainer, tags=['trainer'])
async def get_trainer(username:str):
    response = await get_one_trainer(username)
    if response:
        return response
    raise HTTPException(404, "there is not trainer with this username")

@trainer.post('/trainers', response_model=Trainer, tags=['trainer'])
async def post_trainer(trainer:Trainer):
    response = await create_trainer(trainer.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@trainer.put('/trainers/{id}', response_model=Trainer, tags=['trainer'])
async def put_trainer(id:str,trainer: Trainer):
    response = await update_trainer(id,trainer)
    if response:
        return response
    raise HTTPException(404, "there is not trainer with this username")
    
@trainer.delete('/trainers/{id}', tags=['trainer'])
async def delete_trainer(id:str):
    response = await remove_trainer(id)
    if response:
        return "Succefully deleted trainer"
    raise HTTPException(404, "there is not trainer with this username")
    
