```python


students = []
eligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))

    m1 = float(input("Enter Subject 1 marks: "))
    m2 = float(input("Enter Subject 2 marks: "))
    m3 = float(input("Enter Subject 3 marks: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    students = [m1, m2, m3]

    if (aggregate >= 75 and min(students) >= 60
            and attendance >= 75 and income <= 250000):
        eligible.append(
            (name, aggregate, attendance, income)
        )
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship")


eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- Scholarship Ranking ---")

if len(eligible) == 0:
    print("No eligible students found.")
else:
    print("Rank  Name  Aggregate  Attendance  Family Income")

    for rank, student in enumerate(eligible, start=1):
        name, marks, attendance, income = student

        print(rank, name, marks, attendance, income)

print("\nScholarship allocation completed.")
```
