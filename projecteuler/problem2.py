from utils.TimeIt import TimeIt


def main():
    max_value = 40000

    my_solution(max_value)


    online_answer(max_value)





@TimeIt(10)
def my_solution(max_value):
    memory = [0, 1]
    s = 0
    while True:
        v = memory[-1] + memory[-2]

        if v >= max_value:
            break

        memory.append(v)
        if v % 2 == 0:
            s += v

    return s


@TimeIt(10)
def online_answer(max_value):
    ans = 0
    x = 1  # Represents the current Fibonacci number being processed
    y = 2  # Represents the next Fibonacci number in the sequence
    while x <= max_value:
        if x % 2 == 0:
            ans += x
        x, y = y, x + y
    return str(ans)



if __name__ == '__main__':
    main()
