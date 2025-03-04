from app.Models.pokemon import Pokemon
from app.Models.pokemon_favorite import PokemonFavorites
from app.Models.user import User

class ModelFactory:
    @staticmethod
    def get_model(collection):
        models = {
            "users": User,
            "pokemons": Pokemon,
            "pokemon_favorites": PokemonFavorites
        }
        if collection in models:
            return models[collection]()
        raise ValueError(f"El collecion enviada: {collection} no existe")