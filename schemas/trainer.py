def trainerEntity(trainer) -> dict:
    return {
        "username": trainer["username"],
        "password": trainer["password"],
        "trainer_name": trainer["trainer_name"],
        "pokemon_list": trainer["pokemon_list"]
        
    }
    
def trainersEntity(trainers) -> list:
    return [trainerEntity(trainer) for trainer in trainers]