from app.common.http_methods import GET, POST, PUT
from app.services.base import BaseService
from flask import Blueprint, request

from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)

ingredient_service = BaseService(controller=IngredientController)

@ingredient.route('/', methods=POST)
def create_ingredient():
    return ingredient_service.create(request)

@ingredient.route('/', methods=PUT)
def update_ingredient():
    return ingredient_service.update(request)

@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return ingredient_service.get_by_id(_id)

@ingredient.route('/', methods=GET)
def get_ingredients():
    return ingredient_service.get_all()
