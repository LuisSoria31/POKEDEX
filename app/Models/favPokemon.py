from app import mongo

class FavPokemon:
    collection = mongo.db.favPokemons

    @staticmethod
    def find_all():
        favPokemons = FavPokemon.collection.find()
        return list(favPokemons)
    
    @staticmethod
    def find_by_id(favPokemon_id):
        favPokemon = FavPokemon.collection.find_one({
            "_id": favPokemon_id
        })
        return favPokemon
    @staticmethod
    def create(data):
        favPokemon = FavPokemon.collection.insert_one(data)
        return favPokemon.inserted_id
    
    @staticmethod
    def update(favPokemon_id, data):
        favPokemon = FavPokemon.collection.update_one({
            "_id":favPokemon_id
        },{
            "$set":data
        })
        return favPokemon
    
    @staticmethod
    def delete(favPokemon_id):
        return FavPokemon.collection.delete_one({"_id":favPokemon_id})
