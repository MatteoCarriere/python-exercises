# Exercise: 1
# Task: Fix the job seeker printout — replace comma notation with f-strings
#       to get exact spacing (no auto-inserted spaces around punctuation)

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old")
print()
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})")
print()
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")
