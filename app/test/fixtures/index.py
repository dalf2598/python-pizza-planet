import pytest


@pytest.fixture
def index(client) -> dict:
    response = client.get('/')
    return response
