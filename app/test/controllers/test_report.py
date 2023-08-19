import pytest
from app.controllers import ReportController
from app.controllers.order import OrderController
from app.utils.constants import Constants
from app.utils.db_script import check_db_data

def test_insert_fake_data(app):
    check_db_data()
    ReportController.insert_fake_data()
    orders_from_db, error_orders = OrderController.get_all()

    pytest.assume(error_orders is None)
    pytest.assume(len(orders_from_db) == Constants.NUMBER_OF_FAKE_ORDERS)

def test_get_report(app):
    check_db_data()
    ReportController.insert_fake_data()
    response = ReportController.get_report()
    report = response.json

    pytest.assume(len(report['customers']) == 3)
    pytest.assume(len(report['sales']) == 1)
    pytest.assume(len(report['ingredients']) == 1)