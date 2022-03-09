student_dict = {
    "student": ["Ervin", "Emel", "Malik"],
    "score": [56, 76, 98]
}

#Looping through dict

# for (key, value) in student_dict.items():
#     print(key, value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#loop over dataframes
# for key, value in student_data_frame.items():  #not useful...
    # print(key)
    # print(value)

#using padnas loops
for (index, row) in student_data_frame.iterrows():
    print(row.student, row.score)
    # print(index)