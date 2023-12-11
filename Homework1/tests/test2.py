import pytest
import os
from Homework1.tasks.task2 import find_maximum_and_minimum
path = os.path.dirname(os.path.abspath(__file__)) + "/file_name"


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (path, (1, 6)),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
