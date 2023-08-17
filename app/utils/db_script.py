import json
import logging
import sys
from app.controllers.ingredient import IngredientController
from app.controllers.beverage import BeverageController
from app.controllers.size import SizeController
from app.utils.constants import Constants

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

def is_table_empty(controller):
    rows, _ = controller.get_all()
    return len(rows) == 0

def get_data(path, data):
    with open(path) as json_file:
        response = json.load(json_file)
    return response[data]

def create_data(controller, data):
    for item in data:
        controller.create(item)

def check_data(controller, path, data):
    if is_table_empty(controller):
        try:
            rows = get_data(path, data)
            create_data(controller, rows)
            logger.info(f'{data} created')
        except Exception as ex:
            logger.error(ex)

def check_db_data():
    check_data(SizeController, Constants.SIZES_FILE_PATH, 'sizes')
    check_data(IngredientController, Constants.INGREDIENTS_FILE_PATH, 'ingredients')
    check_data(BeverageController, Constants.BEVERAGES_FILE_PATH, 'beverages')
    logger.info("Data checked")