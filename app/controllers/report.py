import random
import json
from flask import jsonify
from datetime import datetime, timedelta
from app.controllers.beverage import BeverageController
from app.controllers.ingredient import IngredientController

from app.controllers.order import OrderController
from app.controllers.size import SizeController
from app.utils.constants import Constants


class ReportController():

    @staticmethod
    def handle_detail(detail, ingredients):

        for item in detail:
            ingredient = item.get('ingredient')
            if ingredient:
                ingredients[ingredient['name']] = ingredients.get(ingredient['name'], 0) + 1

        return ingredients

    @staticmethod
    def sort_dict_by_value(dict):
        sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        return sorted_dict

    @staticmethod
    def format_response(items, key, value):
        return [{
            key: item[0],
            value: item[1]
        } for item in items]

    @staticmethod
    def parse_date(date_string):
        try:
            return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")

    @staticmethod
    def get_clients():
        with open(Constants.CLIENTS_FILE_PATH) as json_file:
            data = json.load(json_file)
        return data['clients']

    @staticmethod
    def get_random_datetime():
        # Get a random datetime between start of year and now
        today = datetime.now().date()
        start_of_year = datetime(today.year, 1, 1).date()
        days_range = (today - start_of_year).days
        random_days = random.randint(0, days_range)
        random_datetime = start_of_year + timedelta(days=random_days)

        return random_datetime

    @classmethod
    def get_report(cls):
        customers = {}
        montly_sales = {}
        ingredients = {}

        orders = OrderController.get_all()[0]
        for order in orders:
            name = order['client_name']
            date = cls.parse_date(order['date']).strftime("%Y-%m")
            total = order['total_price']

            customers[name] = customers.get(name, 0) + 1
            montly_sales[date] = round(montly_sales.get(date, 0) + total, 2)

            ingredients = cls.handle_detail(order['detail'], ingredients)

        top_three_customers = cls.sort_dict_by_value(customers)[:3]
        top_monthly_revenue = cls.sort_dict_by_value(montly_sales)[:1]
        top_requested_ingredient = cls.sort_dict_by_value(ingredients)[:1]

        return jsonify({
            'customers': cls.format_response(top_three_customers, 'name', 'orders'),
            'sales': cls.format_response(top_monthly_revenue, 'month', 'revenue'),
            'ingredients': cls.format_response(top_requested_ingredient, 'name', 'requests'),
        })

    @classmethod
    def create_order(cls, clients, sizes, ingredients, beverages):
        random_client = random.choice(clients)
        random_size = random.choice(sizes)
        random_ingredients = random.sample(ingredients, random.randint(2, 5))
        random_beverage = random.sample(beverages, random.randint(1, 2))
        random_datetime = cls.get_random_datetime()

        return {
            **random_client,
            'date': random_datetime,
            'size_id': random_size,
            'ingredients': random_ingredients,
            'beverages': random_beverage
        }

    @classmethod
    def create_orders(cls, quantity):
        clients = cls.get_clients()
        sizes = [size['_id'] for size in SizeController.get_all()[0]]
        ingredients = [ingredient['_id'] for ingredient in IngredientController.get_all()[0]]
        beverages = [beverage['_id'] for beverage in BeverageController.get_all()[0]]

        orders = []

        for _ in range(quantity):
            orders.append(cls.create_order(clients, sizes, ingredients, beverages))

        return orders

    @classmethod
    def insert_fake_data(cls):
        orders = cls.create_orders(Constants.NUMBER_OF_FAKE_ORDERS)
        for order in orders:
            OrderController.create(order)
        return jsonify({'message': f'{Constants.NUMBER_OF_FAKE_ORDERS} fake records inserted successfully'})
