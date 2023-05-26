from fastapi import APIRouter, HTTPException
from models.pokemon import Pokemon
from database.pokemon import (
    get_all_pokemons,
    get_all_pokemons_by_region,
    get_one_pokemon,
    create_pokemon,
    update_pokemon,
    remove_pokemon
)
import random

pokemon = APIRouter()


@pokemon.get('/pokemons/{id}', response_model=Pokemon, tags=['pokemon'])
async def get_pokemon(id):
    response = await get_one_pokemon(int(id))
    if response:
        return response
    raise HTTPException(404, "there is not pokemon with this id")


@pokemon.get('/pokemons', response_model=list[Pokemon], tags=['pokemon'])
async def get_pokemons():
    return await get_all_pokemons()


@pokemon.get('/pokemons/region/{region}', response_model=list[Pokemon], tags=['pokemon'])
async def get_pokemons_region(region: str):
    return await get_all_pokemons_by_region(region)


@pokemon.post('/pokemons', response_model=Pokemon, tags=['pokemon'])
async def post_pokemon(pokemon: Pokemon):
    response = await create_pokemon(pokemon.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@pokemon.put('/pokemons/{id}', response_model=Pokemon, tags=['pokemon'])
async def put_pokemon(id, pokemon: Pokemon):
    response = await update_pokemon(int(id), pokemon.dict())
    if response:
        return response
    raise HTTPException(404, "there is not pokemon with this id")


@pokemon.delete('/pokemons/{id}', tags=['pokemon'])
async def delete_pokemon(id):
    response = await remove_pokemon(int(id))
    if response:
        return "Succefully deleted pokemon"
    raise HTTPException(404, "there is not pokemon with this id")


@pokemon.get('/pokemons/random/{region}', response_model=Pokemon, tags=['pokemon'])
async def generate_random_pokemon(region: str):
    value = 0
    if region.upper() == "KANTO":
        value = random.randint(1, 151)
    elif region.upper() == "JOHTO":
        value = random.randint(152, 251)
    elif region.upper() == "HOENN":
        value = random.randint(252, 386)
    elif region.upper() == "SINNOH":
        value = random.randint(387, 493)
    elif region.upper() == "TESELIA":
        value = random.randint(494, 649)
    elif region.upper() == "KALOS":
        value = random.randint(650, 721)
    elif region.upper() == "ALOLA":
        value = random.randint(722, 809)
    pokemon = await get_one_pokemon(value)
    if pokemon:
        return pokemon
    raise HTTPException(400, "Something was wrong")
