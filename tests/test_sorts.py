from spbu_sorting import b_sort, h_sort, m_sort, q_sort
import pytest


TEST_CASES = [
    ([], [], "empty list"),
    ([1], [1], "one elem"),
    ([1, 1], [1, 1], "two elem"),
    ([1, 2, 3], [1, 2, 3], "already sorted"),
    ([3, 2, 1], [1, 2, 3], "reversed"),
    ([1, 3, 2], [1, 2, 3], "mixed")
]

SORTING_FUNCTIONS = [
    (b_sort, "bubble_sort"),
    (h_sort, "heap sort"),
    (m_sort, "merge sort"),
    (q_sort, "quick sort")
]

@pytest.mark.parametrize("arr,expected,test_name", TEST_CASES)
@pytest.mark.parametrize("function,func_name", SORTING_FUNCTIONS)
def test_preliminary(arr, expected, test_name, function, func_name):
    assert function(arr) == expected


@pytest.mark.parametrize("function, func_name", SORTING_FUNCTIONS)
def test_small_random(function, func_name, small_random_list):
    arr = small_random_list
    assert function(arr) == sorted(arr)


@pytest.mark.parametrize("function, func_name", SORTING_FUNCTIONS)
def test_big_random(function, func_name, big_random_list):
    arr = big_random_list
    assert function(arr) == sorted(arr)


@pytest.mark.parametrize("function, func_name", SORTING_FUNCTIONS)
def test_random_size(function, func_name, random_size_list):
    arr = random_size_list
    assert function(arr) == sorted(arr)
