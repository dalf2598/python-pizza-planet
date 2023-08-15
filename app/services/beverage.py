from app.common.http_methods import GET, POST, PUT
from app.services.base import BaseService
from flask import Blueprint, request

from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)

beverage_service = BaseService(controller=BeverageController)

@beverage.route('/', methods=POST)
def create_size():
    return beverage_service.create(request)

@beverage.route('/', methods=PUT)
def update_size():
    return beverage_service.update(request)

@beverage.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return beverage_service.get_by_id(_id)

@beverage.route('/', methods=GET)
def get_sizes():
    return beverage_service.get_all()