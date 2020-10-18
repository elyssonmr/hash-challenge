import pytest
from unittest.mock import Mock, patch
from datetime import date, timedelta

from discount_calculator.services import DiscountCalculator


@pytest.fixture
def black_friday():
    with patch(
        'discount_calculator.services.discount_calculator.date'
    ) as patched:
        patched.today.return_value = date(2020, 11, 25)
        patched.side_effect = date
        yield patched.today


@pytest.fixture
def not_black_friday():
    with patch(
        'discount_calculator.services.discount_calculator.date'
    ) as patched:
        patched.today.return_value = date(2020, 11, 18)
        patched.side_effect = date
        yield patched.today

@pytest.fixture
def user_db():
    return Mock()


@pytest.fixture
def yesterday():
    return date.today() - timedelta(days=1)


@pytest.fixture
def product_db():
    product_db = Mock()
    product_db.find_one.return_value = {'price_in_cents': 10000}

    return product_db


@pytest.fixture
def calculator(user_db, product_db):
    db_mock = {
        'users': user_db,
        'products': product_db
    }
    return DiscountCalculator(db_mock)


def test_should_not_give_discount(calculator, user_db, product_db, yesterday):
    user_id = 'not_your_birthday_id'
    product_id = 'product_costing_100'
    user_db.find_one.return_value = {'date_of_birth': yesterday}

    discount = calculator.calculate_discount(product_id, user_id)

    assert discount == 0
    user_db.find_one.assert_called_once_with({'id': user_id})
    product_db.find_one.assert_called_once_with({'id': product_id})


def test_should_give_10_percent_discount(
    calculator,
    user_db,
    product_db,
    black_friday
):
    user_id = 'not_your_birthday_id'
    product_id = 'product_costing_100'
    user_db.find_one.return_value = {'date_of_birth': yesterday}

    discount = calculator.calculate_discount(product_id, user_id)

    assert discount == 1000


def test_should_give_5_percent_discount(
    calculator,
    user_db,
    product_db,
    not_black_friday
):
    user_id = 'your_birthday_id'
    product_id = 'product_costing_100'
    user_db.find_one.return_value = {'date_of_birth': not_black_friday()}

    discount = calculator.calculate_discount(product_id, user_id)

    assert discount == 500


def test_should_give_max_10_percent_discount(
    calculator,
    user_db,
    product_db,
    black_friday
):
    user_id = 'your_birthday_id'
    product_id = 'product_costing_100'
    user_db.find_one.return_value = {'date_of_birth': black_friday()}

    discount = calculator.calculate_discount(product_id, user_id)

    assert discount == 1000
