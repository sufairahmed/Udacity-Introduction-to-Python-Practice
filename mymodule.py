def line(num):
    temp_num = num
    for i in range(0,temp_num):
        x="+-+-"*num
        return ('\n'+ x + '\n')


def empty_line(empty_line_arg=5):
    empty_line = empty_line_arg
    for i in range(0,empty_line):
        #x= '\n'*empty_line
        return ('\n'*empty_line)

# x = line(20)
# print(x)

# X = new_line()
# print(X)
# print("done")
