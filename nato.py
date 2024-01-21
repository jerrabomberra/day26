nato = [
    "alpha",
    "bravo",
    "charlie",
    "delta",
    "echo",
    "fox-trot",
    "golf",
    "hotel",
    "india",
    "juliet",
    "kilo",
    "lima",
    "mike",
    "november",
    "oscar",
    "papa",
    "quebec",
    "romeo",
    "sierra",
    "tango",
    "uniform",
    "victor",
    "whiskey",
    "x-ray",
    "yankee",
    "zulu",
]
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
nato_alpha = {}
for key in alphabet:
    for value in nato:
        nato_alpha[key.upper()] = value
        nato.remove(value)
        break

print(nato_alpha)

# for key, value in nato_alpha.items():
# #     print(key, value)

# import pandas as pd

# student_dict = {"Student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}
# student_data_frame = pd.DataFrame(student_dict)
# # print(student_data_frame)
# for index, row in student_data_frame.iterrows():
#     print(row.student, row.score)
