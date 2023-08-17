#  Python program to check if the number is an armstrong number or not.

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num #153 15 1
while temp > 0:
    digit = temp % 10 #3 5 1
    sum += digit ** 3 #27 125 1
    temp //= 10 

# display the result
if num == sum:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")