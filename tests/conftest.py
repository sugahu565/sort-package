import pytest
from random import randint


@pytest.fixture
def small_random_list():
    return [randint(-100, 100) for _ in range(100)]


@pytest.fixture
def big_random_list():
    return [randint(-10000, 10000) for _ in range(5000)]


@pytest.fixture
def random_size_list():
    return [randint(-1000, 1000) for _ in range(randint(1, 1000))]

