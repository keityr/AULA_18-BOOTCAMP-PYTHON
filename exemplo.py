

def pegar_pokemon(id:int) -> PokemonSchema:
    response =  requests.get(url=f'https://pokeapi.co/api/v2/pokemon/{id}')
    data= response.json()
    data_types = data['types']
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type'] ['name'])
    types = ','.join(types_list)
    return PokemonSchema(nome=data['name'], type=types)


if __name__=='__main__':
    print(pegar_pokemon(12))
    print(pegar_pokemon(14))
    print(pegar_pokemon(17))
    
