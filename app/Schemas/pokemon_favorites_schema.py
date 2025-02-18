from marshmallow import Schema, fields, ValidationError

class PokemonFav(Schema):
    name = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El nombre es requerido"
        }
    )

    id = fields.Int(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El ID es requerido"
        }
    )