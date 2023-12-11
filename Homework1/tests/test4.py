import pytest
from Homework1.tasks.task4 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "k",  "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([7, -3, 4, 1, 3, 13, -4, 1], 4, 21),
        ([-1, -2, -3, -4, -3, -1, -2, -4], 3, -6),
        ([-2, -3, -5, 8, -1, -2, -9, -5, 0], 4, 0)
    ]
)
def test_check_sum_of_four(value: list, k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(value, k)

    assert actual_result == expected_result
