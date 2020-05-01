import itertools

import numpy as np
import tqdm

from projecteuler.eulerlib import factorize, ceil_sqrt


def main():
    print(my_solution())

def my_solution():
    n = 500
    traingle_number = 0

    for i in tqdm.tqdm(itertools.count(1)):
        traingle_number += i
        amount = len(factorize(traingle_number))

        if amount >= n:
            return traingle_number





if __name__ == '__main__':
    main()
