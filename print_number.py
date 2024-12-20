#!/usr/bin/python3
"""will not raise an error if number is not an integer."""
number = 98
print(f"{number} Battery street")


"""will raise an error if number is not an integer."""
number = "98" #will raise an error because variable number holds string
print(f"{number:d} Battery street")