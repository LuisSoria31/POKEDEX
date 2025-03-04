from flask import Blueprint, request
from app.Tools.response_manager import ResponseManager
from app.Schemas.pokemon_favorites_schema import PokemonFavoriteSchema
from marshmallow import ValidationError
from app.Models.factory import ModelFactory
from bson import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity

RM = ResponseManager()
bp = Blueprint("pokemon_favorites", __name__, url_prefix="/pokemons")
pokemon_fav_model= ModelFactory.get_model("pokemon_favorites")
fav_pokemon_schema = PokemonFavoriteSchema()


@bp.route("/", methods=["POST"])
@jwt_required()
def create():
    user_id = get_jwt_identity()
    try:
        data = request.json
        data = fav_pokemon_schema.load(data)
        data["user_id"] = user_id
        pokekemon_fav_id = pokemon_fav_model.create(data)
        return RM.success({"pokemon_fav_id":str(pokekemon_fav_id)})
    except ValidationError as err:
        print(err)
        return RM.error("Los parametros enviados son incorrectos")
    
@bp.route("/delete/<string:pokemon_fav_id>", methods=["DELETE"])
@jwt_required()
def delet(pokemon_fav_id):
    pokemon_fav_model.delete(ObjectId(pokemon_fav_id))
    return RM.success("Pokemon eliminado con exito")

@bp.route("/get/<string:pokemon_fav_id>", methods=["GET"])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    data = pokemon_fav_model.find_by_id(user_id)
    return RM.success(data)