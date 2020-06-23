# this series always subtruced by  its even numbers
user_input = int(input("Enter the length of the series: "))

sum = 0
for i in range(0, user_input):
    # sum = 0
    if i%2 == 1:
        sum = sum + i
    elif i%2 ==0:
        sum = sum - i
        # pass

print(sum)
