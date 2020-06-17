
def sum_of_series(num_series):
    total = 0
    for i in range(0, num_series):
        total = total + i

    print("The sum of the series {} = {}".format(num_series, total))
def sum_of_square_series(num_series):
    total = 0

    total = (num_series * (num_series + 1) * (2 * num_series + 1 )) / 6

    print("The sum of the square series {} = {} ".format(num_series, total))





len_series = int(input("Enter the len of series: "))

sum_of_series(len_series)
sum_of_square_series(len_series)
