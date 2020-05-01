from tqdm import trange
import functools
import sys

def main():
    sys.setrecursionlimit(3000)
    n = 1_000_000

    result = max([(i, collatz_seq_len_recursive(i)) for i in trange(n)], key=lambda x: x[1])
    print(result)
    result = max([(i, collatz_seq_len(i)) for i in trange(n)], key=lambda x: x[1])
    print(result)


def collatz_seq_len(n):
    results = 1

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        results += 1


    return results


@functools.lru_cache(maxsize=1_000_000)
def collatz_seq_len_recursive(n):
    if n < 1:
        return 0
    if n == 1:
        return 1



    x = n // 2 if n % 2 == 0 else 3 * n + 1

    return collatz_seq_len_recursive(x) + 1





if __name__ == '__main__':
    main()
