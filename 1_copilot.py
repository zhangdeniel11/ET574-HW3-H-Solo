# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]

# function to print 'Hi name' for each student in the list
def greet_students(names):
	for name in names:
		print(f"Hi {name}")

# call the function
greet_students(students)
