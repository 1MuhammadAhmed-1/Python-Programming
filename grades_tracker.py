def tot_marks(marks):
    tot_sum = 0
    for i in marks:
        tot_sum += i
    return tot_sum
        

def avg_marks(marks):
    return (tot_marks(marks) / len(marks))


grades = {
    (0, 40.00): "F",       
    (40.01, 60.00): "D",   
    (60.01, 70.00): "C",   
    (70.01, 80.00): "B",   
    (80.01, 90.00): "A",
    (90.01, 100.00): "A+"
}

def get_grade(score):
    for (low, high), grade in grades.items():
        if low <= score <= high:
            return grade

marks = []
for i in range(0 , 3):
    mark = int(input("Enter your marks out of hundred in three subjects: "))
    marks.append(mark)

total_marks = tot_marks(marks)
average_marks = avg_marks(marks)

print(f"Your total marks are: {total_marks}.")
print(f"Your average marks are: {round(average_marks, 2)}.")
print(f"Your grade is: {get_grade(average_marks)}.")