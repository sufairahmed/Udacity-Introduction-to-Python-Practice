import mymodule
ln = mymodule.line(15)

print(ln)

"""
 Question: Write code to check if the numbers provided in the list check_prime
 are prime numbers. For each number, if the number is prime, the code should print
 that the number is a prime number. If the number is NOT a prime number, it should
 print that the number is not a prime number, and also print a factor of that number
 besides 1 and the number itself.
 """
"""
check_prime = [9,26, 39, 51, 53, 57, 79, 85]
#iterate through the check_prime list
for num in check_prime:
    # search for factor through the number ranging from 2 to number list
    for i in range(2,num):
        # number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is not a prime number, because {} is a factor {}".format(num,i,num))
            break
# Otherwise keep chacking until we have reached all possible factor.
        if i == num - 1:
            print("{} is a prime number.".format(num))
"""
# ZIP AND ENUMERATE
letters = ['a','b','c']
nums = ['1','2','3']

for letter, num in zip(letters,nums):
    print("{}:{}".format(letter,num))
# enumerate use if you want index along with each elements
print(ln)
letters = ['a','b','c','d','e']

for i, letter in enumerate(letters):
    print(i,letter)
