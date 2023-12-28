# list comprehension
numbers = [1, 2, 3]
# new_list = [n**2 for n in numbers]
# print(new_list)


# name = "douglas"

# new_list = [letter for letter in name]
# print(new_list)


double = [n * 2 for n in range(1, 5)]
print(double)

list_new = [n**2 for n in range(1, 6)]

names = ["Joe", "Angela", "Caroline", "sebastian", "Elanor"]

short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
