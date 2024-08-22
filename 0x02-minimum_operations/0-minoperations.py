#!/usr/bin/python3
"""Module that creates a function that takes n as an argument"""


def minOperations(n: int) -> int:
    """Returns minimum number of operations"""
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
