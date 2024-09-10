#!/usr/bin/env python3
import time

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    start = time.time()
    result = fib(100)
    end = time.time()
    print(f'Result: {result}\nComputation time: {end - start}')

# Time complexity: O(2**n) || O(2^n)
