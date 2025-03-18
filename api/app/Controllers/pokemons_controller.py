from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.Models.factory import ModelFactory
from bson import ObjectId
from flask_jwt_extended import jwt_required

bp = Blueprint("pokemons", __name__, url_prefix="/pokemon")
pokemon_model= ModelFactory.get_model("pokemons")

@bp.route("/get/<string:pokemon_id>", methods=["GET"])
@jwt_required()
def get_pokemon(pokemon_id):
    pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
    return jsonify(pokemon, 200)

@bp.route("/getAll", methods=["GET"])
@jwt_required()
def get_pokemons():
    pokemon = pokemon_model.find_all()
    return jsonify(pokemon, 200)