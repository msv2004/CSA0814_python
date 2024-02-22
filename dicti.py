
marks_dict = {
    "ravi1": [97, 85, 85, 67],
    "rahul2": [92, 91, 94, 85]
}

total_marks_dict = {}

for student, marks in marks_dict.items():
    total_marks = sum(marks)
    total_marks_dict[student] = total_marks

print("Student-wise total marks:")
for student, total_marks in total_marks_dict.items():
    print(f"{student}: {total_marks}")
