import requests
from db import SessionLocal, engine, Base
from schema import PokemonSchema
from models import Pokemon

Base.metadata.create_all(bind=engine)


def pegar_pokemon(id:int) -> PokemonSchema:
    response =  requests.get(url=f'https://pokeapi.co/api/v2/pokemon/{id}')
    if response.status_code == 200:
        data= response.json()
        data_types = data['types']
        types_list = []
        for type_info in data_types:
            types_list.append(type_info['type'] ['name'])
        types = ','.join(types_list)
        return PokemonSchema(name=data['name'], type=types)
    else: 
        return None

def adiciona_pokemon_no_db(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        # Adiciona à sessão e salva no banco
        db.add(db_pokemon)
        db.commit()

    # Opcional: carrega o usuário salvo com ID atribuído
        db.refresh(db_pokemon) 
    return db_pokemon   