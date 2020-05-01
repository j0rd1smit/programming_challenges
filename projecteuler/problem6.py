
def main():
    n = 100
    squared_number = [i**2 for i in range(1, n + 1)]
    natural_numbers = list(range(1, n + 1))

    result =  sum(natural_numbers) **2 - sum(squared_number)
    print(result)

if __name__ == '__main__':
    main()