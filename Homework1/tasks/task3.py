from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    tup_count = 0
    for i in a:
        for j in b:
            for k in c:
                for m in d:
                    if i + j + k + m == 0:
                        tup_count += 1
    return tup_count
