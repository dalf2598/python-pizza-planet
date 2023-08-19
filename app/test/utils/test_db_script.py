import pytest
from app.controllers.beverage import BeverageController
from app.controllers.ingredient import IngredientController
from app.controllers.size import SizeController
from app.utils.constants import Constants
from app.utils.db_script import check_db_data, get_data


def test_db_script(app):
    check_db_data()
    
    sizes_from_db, error_sizes = SizeController.get_all()
    sizes_from_data_json = get_data(Constants.SIZES_FILE_PATH, 'sizes')
    
    ingredients_from_db, error_ingredients = IngredientController.get_all()
    ingredients_from_data_json = get_data(Constants.INGREDIENTS_FILE_PATH, 'ingredients')

    beverages_from_db, error_beverages = BeverageController.get_all()
    beverages_from_data_json = get_data(Constants.BEVERAGES_FILE_PATH, 'beverages')

    pytest.assume(error_sizes is None)
    pytest.assume(error_ingredients is None)
    pytest.assume(error_beverages is None)
    pytest.assume(len(sizes_from_db) == len(sizes_from_data_json))
    pytest.assume(len(ingredients_from_db) == len(ingredients_from_data_json))
    pytest.assume(len(beverages_from_db) == len(beverages_from_data_json))
