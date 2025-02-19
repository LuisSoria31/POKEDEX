#Crea
#Eliminar
#get all
#Modificar la case del modelo y evitar que se usen metodos indebidos

from flask import Blueprint, request, jsonify
from app.Schemas.pokemon_favorites_schema import PokemonFav
from marshmallow import ValidationError
from app.Models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemons", __name__, url_prefix="/pokemons")
fav_pokemon_schema = PokemonFav()
pokemon_fav_schema = ModelFactory.get_model("pokemons")

@bp.route("/create<string:pokemon_fav_id>", method=["CREATE"])
def create(pokemon_fav_id):
    pokemon_fav_schema.create(ObjectId(pokemon_fav_id))
    return jsonify("Pokemon creado con exito", 200)
    
@bp.route("/delete/<string:pokemon_fav_id>", method=["DELETE"])
def delet(pokemon_fav_id):
    pokemon_fav_schema.delete(ObjectId(pokemon_fav_id))
    return jsonify("Pokemon eliminado con exito", 200)

@bp.route("/get/<string:pokemon_fav_id", method=["GET"])
def get_user(pokemon_fav_id):
    pokemon = pokemon_fav_schema.find_by_id(ObjectId(pokemon_fav_id))
    return jsonify(pokemon, 200)

