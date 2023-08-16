def operation(num_1, num_2, op):
    if op == '+':
        return num_1 + num_2
    elif op == '-':
        return num_1 - num_2
    elif op == '*':
        return num_1 * num_2
    elif op == '/':
        return num_1 / num_2
    else: 
        print("Unknown operation")

num_1 = float(input("Enter the first number: "))
op = input("Enter the operation(+, -, *, /): ")
num_2 = float(input("Enter the second number: "))

print("The output is: ")
print(operation(num_1, num_2, op))