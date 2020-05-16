# my_list = [23, 43, 'sufair','ahmed',90, 100, 'taslima',13]
# print(my_list)
# print(my_list[ :-1])

#month = 8
month =int (input('enter a month no: '))
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[month - 1]

print(num_days)
