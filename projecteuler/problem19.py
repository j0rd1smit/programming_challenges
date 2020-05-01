import datetime

def main():
    date = datetime.datetime(1901, 2, 2)
    end_date = datetime.datetime(2000, 12, 31)
    delta = datetime.timedelta(days=1)

    count = 0
    while date < end_date:
        if date.day == 1 and date.weekday() == 6:
            count += 1
        date += delta


    print(count)


if __name__ == '__main__':
    main()
