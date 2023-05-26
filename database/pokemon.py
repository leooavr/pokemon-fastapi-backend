from models.pokemon import Pokemon
from bson import ObjectId
from database.db import database


collection = database.pokedex

async def get_one_pokemon(id:int):
    pokemon = await collection.find_one({"id": id}, {"_id":0})
    return pokemon


async def get_all_pokemons():
    pokemons = []
    pokemon_collection = collection.find({})
    async for pokemon in pokemon_collection:
        pokemons.append(Pokemon(**pokemon))
    return pokemons

async def get_all_pokemons_by_region(region:str):
    pokemons = []
    pokemon_collection = collection.find({})
    async for pokemon in pokemon_collection:
        if pokemon['region'].upper() == region.upper():
            pokemons.append(Pokemon(**pokemon))
    return pokemons


async def create_pokemon(pokemon: Pokemon):
    new_pokemon = pokemon
    response = await collection.insert_one(new_pokemon)
    if response.acknowledged:
        return new_pokemon
    


def update_pokemon(id: int, pokemon: Pokemon):
    response = collection.find_one_and_update(
        {"id": id}, {"$set": dict(pokemon)})
    return response


async def remove_pokemon(id: int):
    response = await collection.delete_one({"id": id})
    if response.deleted_count == 1:
        return True
    else: 
        return False
