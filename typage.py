from typing import List

def add(a: int,b: int) -> int:
    return a + b

print(add(1,3))

def highest(numbers: List[int]) -> int:
    max_value = 0
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

print(highest([1,0,7,4,23,9,8,5]))

def division(a: float,b: float) -> float:
    assert b != 0 # souvent utiliser dans test
    return a/b

print(division(5,3))

print(__name__)