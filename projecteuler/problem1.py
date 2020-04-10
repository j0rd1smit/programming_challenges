def main():
    print(sum_of_all_mutliple_bellow(1000))


def sum_of_all_mutliple_bellow(n):
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(n)))


if __name__ == '__main__':
    main()
