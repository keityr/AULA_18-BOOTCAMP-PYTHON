from pydantic import BaseModel

class PokemonSchema(BaseModel):#Contrato de dados, View de dados, Schema de dados
    name: str
    type: str

    
    model_config = {
        'from_attributes': True
    }