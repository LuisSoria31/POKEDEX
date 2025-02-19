from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.Models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemons", __name__, url_prefix="/pokemons")
pokemon_model= ModelFactory.get_model("pokemons")

@bp.route("/get/<string:pokemon_id", method=["GET"])
def get_pokemon(pokemon_id):
    pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
    return jsonify(pokemon, 200)

@bp.route("getAll<>", method=["GET_ALL"])
def get_pokemon():
    pokemon = pokemon_model.find_all()
    return jsonify(pokemon, 200)