from pydantic import BaseModel
from models.pokemon import Pokemon

class Trainer(BaseModel):
    username:str
    password: str
    trainer_name: str
    pokemon_list: list[Pokemon]