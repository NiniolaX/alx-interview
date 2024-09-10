#!/usr/bin/env python3
import time
import sys

def fib(n, memo=None, count=0):
    # Initialize dictionary to store values
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n], count
    if n < 2:
        return n, count

    fib_n_1, count = fib(n - 1, memo, count)
    fib_n_2, count = fib(n - 2, memo, count)

    result = fib_n_1 + fib_n_2 
    memo[n] = result

    return result, count + 1

if __name__ == "__main__":
    start = time.time()
    result, count = fib(100)
    end = time.time()
    print(f'Result: {result}\nComputation time: {end - start}') #\nNumber of operations: {count}

# Time complexity => O(2n + 1)

# This fib() can only calculate a max of 998 as the python has a maximum recursion depth of 1000.
print(sys.getrecursionlimit())

