import itertools
import math

from utils.TimeIt import TimeIt


def main():
    #my_solution()
    solution()

@TimeIt()
def my_solution():
    n = 20

    for i in itertools.count(start=n **2, step=n):
        isDivisable = True
        for j in range(n, 0, -1):
            if i % j != 0:
                isDivisable = False
                break

        if isDivisable:
            break
    return i


def solution():
    ans = 1
    for i in range(1, 21):
        ans *= i // math.gcd(i, ans)

    return str(ans)

if __name__ == '__main__':
    main()
