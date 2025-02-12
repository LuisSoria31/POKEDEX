from app import mongo
from app.Models.super_class import SuperClass

class User(SuperClass):
    def __init__(self):
        super().__init__("user")
    
    def find_all(self):
        raise NotImplementedError("No es necesario obtener todos los usuarios")

    
