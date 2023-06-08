from models.trainer import Trainer
from bson import ObjectId
from database.db import database

collection = database.trainer


async def get_one_trainer(username: str):
    trainer = await collection.find_one(({"username": username}))
    return trainer


async def get_all_trainers():
    trainers = []
    trainer_collection = collection.find({})
    async for trainer in trainer_collection:
        trainers.append(Trainer(**trainer))
    return trainers


async def create_trainer(trainer: Trainer):
    new_trainer = trainer
    result = await collection.insert_one(new_trainer)
    return new_trainer


async def update_trainer(id: str, trainer: Trainer):
    response = collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(trainer)})
    if response.modified_count == 1:
        return collection.find_one({"_id": ObjectId(id)})


async def remove_trainer(id: str):
    response = await collection.delete_one({"_id": ObjectId(id)})
    if response.deleted_count == 1:
        return True
    else:
        return False
