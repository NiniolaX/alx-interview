#!/usr/bin/python3

def factorize(n: int) -> list:
    prime_factors = []
    divisor = 2

    while n != 1:
        while n % divisor == 0:
            n //= divisor
            prime_factors.append(divisor)
        divisor += 1

    return prime_factors

if __name__ == "__main__":
    print(factorize(360))

# PSEUDO CODE
