numbers = [3, 4, 7, 11, 3]
print(numbers)
print(numbers[1])
print(numbers[-1])

numbers[1] = 2 # this change de number with the index [1] to 2
print(numbers) 

del numbers[1] # this delete de number with the index [1]
print(numbers)

numbers[1] = numbers[2]
print(numbers)

print(len(numbers)) # this print the length of the lists

numbers.append(17) # this add the number 17 to the end of the list
print(numbers)

numbers.insert(2, 21) # this add the number 21 to index number 2
print(numbers)

numbers.sort() # this order the numbers in ascending
print(numbers)