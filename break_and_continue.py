user_name = input("what is your username: ").upper()
name = ""
for letter in user_name:
    if letter in "AEIOU":
        continue
    name += letter
print(name.capitalize())