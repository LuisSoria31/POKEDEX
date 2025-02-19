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
pokemon_fav_model= ModelFactory.get_model("pokemons")


@bp.route("/register", methods=["POST"])
def register():
    try:
        data = fav_pokemon_schema.load(request.json)
        pokekemon_fav_id = pokemon_fav_model.create(data)
        return jsonify({"pokemon_fav_id":str(pokekemon_fav_id)}, 200)
    except ValidationError as err:
        return jsonify("los parametros enviados son incorrectos", 400)
    
@bp.route("/delete/<string:pokemon_fav_id>", method=["DELETE"])
def delet(pokemon_fav_id):
    pokemon_fav_model.delete(ObjectId(pokemon_fav_id))
    return jsonify("Pokemon eliminado con exito", 200)

@bp.route("/get/<string:pokemon_fav_id", method=["GET"])
def get_user(pokemon_fav_id):
    pokemon = pokemon_fav_model.find_by_id(ObjectId(pokemon_fav_id))
    return jsonify(pokemon, 200)