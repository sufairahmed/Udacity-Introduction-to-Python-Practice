# find sum of series 123 + 234+ 345 + . . . + n(n+1)(n+2)
def sum_of_series(ser_len):
    tot = 0
    i = 1
    # for i in range(0,ser_len):
    while i<=ser_len:
        tot = tot + i * (i+1) *(i+2)
        i = i +1

    return tot

user_input = int (input("enter the length of series: "))
print(sum_of_series(user_input))
