from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        line = fi.readline()
        f = line.strip().split(",")
        num = list(map(int, f))
        max_num = max(num)
        min_num = min(num)
        res_nums = (min_num, max_num)

        return res_nums
