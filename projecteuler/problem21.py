from projecteuler.eulerlib import factorize


def main():
    res = 0
    for i, v in enumerate(amicable_number_seq()):
        if v >= 10_000:
            break
        res += v

    print(res)



def amicable_number_seq():
    i = 0
    while True:
        a = sum(factorize(i).difference({i}))
        b = sum(factorize(a).difference({a}))
        if i == b and i != a:
            yield i
        i += 1

if __name__ == '__main__':
    main()
