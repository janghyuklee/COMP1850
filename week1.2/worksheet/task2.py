# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

list = read_numbers()

if not list:
    sys.exit("Error: no numbers provided ")

list.sort()

print(list)

minimum = list[0]
maximum = list[-1]
mean = sum(list) / len(list)
median = list[len(list) // 2] if len(list) % 2 != 0 else (list[len(list) // 2 - 1] + list[len(list) // 2]) / 2

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Mean: {mean}")
print(f"Median: {median}")
