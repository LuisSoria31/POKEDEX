from app.Models.pokemon import Pokemon
from app.Models.pokemon_favorite import PokemonFavorites
from app.Models.user import User

class ModelFactory:
    @staticmethod
    def get_model(collection_name):
        models = {
            "users": User,
            "pokemons": Pokemon,
            "pokemon_favorites": PokemonFavorites
        }
        if collection_name in models:
            return models[collection_name]()
        raise ValueError(f"El collecion enviada: {collection_name} no existe")