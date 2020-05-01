import itertools
import math


def main():
    fact = math.factorial(100)
    res = sum(map(lambda x: int(x), str(fact)))

    print(res)


if __name__ == '__main__':
    main()
