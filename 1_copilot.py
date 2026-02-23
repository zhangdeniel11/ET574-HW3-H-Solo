# list of three students named Jon, Kim and Lee
# The list can be modified (append/remove) at runtime.

students = ["Jon", "Kim", "Lee"]

# Add Sara and Miko to the list after it is created
students.append("Sara")
students.append("Miko")


# function to print 'Hi name' for each student in the list

def greet_students(names):
	"""Print a greeting for each name in the iterable `names`.

	Args:
		names: An iterable of strings representing student names.
	"""
	# Iterate through each student name and print a formatted greeting
	for name in names:
		# f-string inserts the current `name` into the greeting
		print(f"Hi {name}")

	# After greeting everyone, print the total count
	print(f"Total number of students: {len(names)}")


# call the function with our `students` list
# Output:
# Hi Jon
# Hi Kim
# Hi Lee
greet_students(students)
