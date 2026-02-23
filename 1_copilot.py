# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]

# change Jon to John
students[0] = 'John'

# Add Sara and Miko to the list after it is created
students.append("Sara")
students.append("Miko")

# function to print 'Hi name' for each student in the list
def greet_students(names):
    for name in names:
        print(f"Hi {name}")
    print(f"Total number of students: {len(names)}")

# call the function
greet_students(students)