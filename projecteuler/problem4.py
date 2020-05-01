import math

from utils.TimeIt import TimeIt


def main():
    my_solution()
    online_solution()

@TimeIt()
def online_solution():
    ans = max(i * j
              for i in range(100, 1000)
              for j in range(100, 1000)
              if str(i * j) == str(i * j)[:: -1])
    return str(ans)

@TimeIt()
def my_solution():
    best_value = 0
    numbers_range = list(range(100, 999))
    for i in numbers_range:
        for j in numbers_range:
            n = i * j
            if is_palindromic_number(n):
                best_value = max(best_value, n)

    return best_value


def is_palindromic_number(n):
    n = str(n)
    if len(n) == 1:
        return True

    if len(n) % 2 == 0:
        mid_point = len(n) // 2
        return n[:mid_point] == n[mid_point:][::-1]
    else:
        mid_point = len(n) // 2
        return n[:mid_point] == n[mid_point+1:][::-1]

if __name__ == '__main__':
    main()
