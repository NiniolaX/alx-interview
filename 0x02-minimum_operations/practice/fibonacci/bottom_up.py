#!/usr/bin/env python3
import time

def fib(n, memo={}):
    for i in range(n + 1):
        if i == 0:
            memo[i] = 0
        elif i == 1 or i == 2:
            memo[i] = 1
        else:
            memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

if __name__ == "__main__":
    start = time.time()
    result = fib(100)
    end = time.time()
    print(f'Result: {result}\nComputation time: {end - start}')

# Time complexity => O(n)
