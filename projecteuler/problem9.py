import math

def main():
    n = 1000

    for a in range(1, n):
        for b in range(a + 1, n):
            c2= a**2 + b**2
            c = math.sqrt(c2)
            if a + b + c == n:
                print(a, b, c)
                print(a * b * c)


if __name__ == '__main__':
    main()
