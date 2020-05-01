def main():
    n = 1000
    print(2 ** n)
    result = sum([int(i) for i in str(2 ** n)])
    print(result)


if __name__ == '__main__':
    main()
