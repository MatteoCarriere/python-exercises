# Exercise: 8
# Task: Write a program which asks for the number of students on a course and the desired group size

student_per_course = int(input("How many students on the course? "))
desired_size = int(input("Desired group size? "))

num_of_groups = student_per_course // desired_size

# If there are leftovers, students add one more group
if student_per_course % desired_size != 0:
    num_of_groups += 1

print(f"Number of groups formed: {num_of_groups}")