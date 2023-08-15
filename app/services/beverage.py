from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)

@beverage.route('/', methods=POST)
def create_size():
    size, error = BeverageController.create(request.json)
    response = size if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@beverage.route('/', methods=PUT)
def update_size():
    size, error = BeverageController.update(request.json)
    response = size if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@beverage.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    size, error = BeverageController.get_by_id(_id)
    response = size if not error else {'error': error}
    status_code = 200 if size else 404 if not error else 400
    return jsonify(response), status_code

@beverage.route('/', methods=GET)
def get_sizes():
    sizes, error = BeverageController.get_all()
    response = sizes if not error else {'error': error}
    status_code = 200 if sizes else 404 if not error else 400
    return jsonify(response), status_code