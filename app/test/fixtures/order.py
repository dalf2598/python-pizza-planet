import pytest

from ..utils.functions import (shuffle_list, get_random_sequence,
                               get_random_string)


def client_data_mock() -> dict:
    return {
        'client_address': get_random_string(),
        'client_dni': get_random_sequence(),
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def create_order(client, order_uri, create_size, create_ingredients, create_beverages, client_data) -> dict:
    size_id = create_size.json.get('_id')
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]

    response = client.post(order_uri, json={
        **client_data_mock(),
        'size_id': size_id,
        'ingredients': ingredients,
        'beverages': beverages,
    })
    return response

@pytest.fixture
def create_orders(client, order_uri, create_sizes, create_ingredients, create_beverages) -> list:
    sizes = [size.get('_id') for size in create_sizes]
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    
    orders = []
    for _ in range(10):
        new_order = client.post(order_uri, json={
            **client_data_mock(),
            'size_id': shuffle_list(sizes)[0],
            'ingredients': shuffle_list(ingredients)[:5],
            'beverages': shuffle_list(beverages)[:5],
        })
        orders.append(new_order.json)
    return orders
