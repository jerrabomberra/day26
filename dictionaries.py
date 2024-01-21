# import random

# # dictionaries

# first = {
#     "Doug": 70,
#     "Bob": 85,
#     "Vatch": 64,
# }


# # print(first.items())

# # for key, item in first.items():
# #     print(key, item)

# # print(first["Doug"])
# first["Jill"] = 87
# print(first)
# first.clear()
# print(first)

# # new_dict = {new_key : new_value for item in list}

# # new_dict = {new_key: new_value for (key, value) in dict.items() if test}

# names = ["Bob", "Jill", "Jack", "Betty", " Dave", "Beth", "Alex", "Fred"]

# student_scores = {student: random.randint(31, 100) for student in names}
# print(student_scores)

# passed_students = {
#     student: score for (student, score) in student_scores.items() if score >= 0
# }
# print(passed_students)

d = {}  # empty dictionary

numNames = {1: "One", 2: "Two", 3: "Three"}  # int key, string value

decNames = {
    1.5: "One and Half",
    2.5: "Two and Half",
    3.5: "Three and Half",
}  # float key, string value

items = {
    ("Parker", "Reynolds", "Camlin"): "pen",
    ("LG", "Whirlpool", "Samsung"): "Refrigerator",
}  # tuple key, string value

romanNums = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}  # string key,
romanNums["VI"] = 6
romanNums["0"] = 0
print(romanNums)
new_romans = {key: value for (key, value) in romanNums.items() if value % 2 == 0}
print(new_romans)
