import pytest


def test_db_status(index):
    db_status = index.json
    pytest.assume(db_status['error'] == '')
    pytest.assume(db_status['status'] == 'up')
    pytest.assume(db_status['version'] == '0.0.2')