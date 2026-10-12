# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

number = read_numbers()

if not number:
    sys.exit("Error: no numbers provided ")

number.sort()

print(number)

minimum = number[0]
maximum = number[-1]
mean = sum(number) / len(number)
median = number[len(number) // 2] if len(number) % 2 != 0 else (number[len(number) // 2 - 1] + number[len(number) // 2]) / 2

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Mean: {mean}")
print(f"Median: {median}")
