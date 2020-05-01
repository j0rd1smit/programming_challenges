def main():
    n = 1000
    my_res  = my_solution(n)

    print(my_res)


def my_solution(n):
    amount = sum([len(number_to_word(i)) for i in range(1, n + 1)])
    return amount


def number_to_word(n):
    nums_to_word = {1: 'One',
                    2: 'Two',
                    3: 'Three',
                    4: 'Four',
                    5: 'Five',
                    6: 'Six',
                    7: 'Seven',
                    8: 'Eight',
                    9: 'Nine',
                    10: 'Ten',
                    11: 'Eleven',
                    12: 'Twelve',
                    13: 'Thirteen',
                    14: 'Fourteen',
                    15: 'Fifteen',
                    16: 'Sixteen',
                    17: 'Seventeen',
                    18: 'Eighteen',
                    19: 'Nineteen',
                    20: "Twenty",
                    30: 'Thirty',
                    40: 'Forty',
                    50: 'Fifty',
                    60: 'Sixty',
                    70: 'Seventy',
                    80: 'Eighty',
                    90: 'Ninety',
                    }

    if n <= 19:
        return nums_to_word[n]
    if n < 100:
        div, mod = divmod(n, 10)
        res = nums_to_word[div * 10]
        if mod != 0:
            res += number_to_word(mod)
        return res
    if n < 1000:
        div, mod = divmod(n, 100)
        res = nums_to_word[div] + "Hundred"
        if mod != 0:
            res += "And" + number_to_word(mod)
        return res

    if n < 10000:
        div, mod = divmod(n, 1000)
        res = nums_to_word[div] + "Thousand"
        if mod != 0:
            res += number_to_word(mod)
        return res

    raise Exception(f"n > 1000 are not supported your n = {n}")


if __name__ == '__main__':
    main()
