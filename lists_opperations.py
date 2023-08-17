list_1 = [3, 4, 7, 11, 3]

# the list starts in index 0 and not include the last element
list_2 = list_1[0:-1] 
print(list_1, list_2)

# the list starts in index 0 and include the last element
list_2 = list_1[:] 
print(list_1, list_2)

# agregate a new element in the list
# the lists doesn't the same so the element only appears in the list_2
list_2.append(33)
print(list_1, list_2)

# with this the lists are the same
list_2 = list_1
print(list_1, list_2)

# so the element appears in both lists
list_2.append(27)
print(list_1, list_2)