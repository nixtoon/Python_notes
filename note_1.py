print("Enter 2 numbers to see what is the largest")
num_1 = float(input("Input the first number: "))
num_2 = float(input("Input the second number: "))
num_3 = float(input("Input the third number: "))

if num_1 >= num_2 and num_1 >= num_3: 
  print(str(num_1) + " is the largest  number") 
elif num_2 >= num_3:
  print(str(num_2) + " is the largest  number") 
else:
  print(str(num_3) + " is the largest number")