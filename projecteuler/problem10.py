import projecteuler.eulerlib as eulerlib
import numpy as np


def main():
    n = 2_000_000
    print(np.sum(eulerlib.list_primes(n)))



if __name__ == '__main__':
    main()
