import itertools


def main():
    n = 10_001
    primes = [2]
    for i in itertools.count(3, 2):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

        if len(primes) == n:
            break

    print(primes[-1])


if __name__ == '__main__':
    main()
