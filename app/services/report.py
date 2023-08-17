from app.common.http_methods import GET, POST
from flask import Blueprint
from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/', methods=POST)
def insert_fake_data():
    return ReportController.insert_fake_data()

@report.route('/', methods=GET)
def get_report():
    return ReportController.get_report()    
