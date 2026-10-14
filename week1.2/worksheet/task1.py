# Worksheet 1.2: Task 1 Solution
import sys

grade = input("Please enter your grade: ")

while not grade.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100 ")

while int(grade) < 0 or int(grade) > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100 ")

if int(grade) <= 39:
    print(grade + " is a Fail ")

if int(grade) >= 40 and int(grade) <= 69:
    print(grade + " is a Pass ")

if int(grade) >= 70 and int(grade) <= 100:
    print(grade + " is a Distinction ")
