def main():
    prime_factors = []
    v = 600851475143
    seq = seq_of_primes()
    next_prime = next(seq)
    while True:

        if v % next_prime == 0:
            v = v / next_prime
            prime_factors.append(next_prime)
        else:
            next_prime = next(seq)
        if v == 1:
            break

    print(prime_factors)



def prime_factor(n):
    primes = [3]
    for i in range(5, n):
        i_is_prime = True
        for prime in primes:
            if i % prime == 0:
                i_is_prime = False
                break
        if i_is_prime:
            primes.append(i)

    return primes

def seq_of_primes():
    primes = [3]
    i = 5
    while True:
        i_is_prime = True
        for prime in primes:
            if i % prime == 0:
                i_is_prime = False
                break
        if i_is_prime:
            yield primes[-1]
            primes.append(i)

        i += 1

if __name__ == '__main__':
    main()
