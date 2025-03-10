import os
import sys
import json
import logging
import requests  # Unused import (Fails Unused Imports Test)

AWS_SECRET_ACCESS_KEY = "XYZ123"  # Hardcoded Secret (Fails Security Test)

# No function definition (Fails Function Definition Check)
print("Hello, World!")

# No try-except block (Fails Exception Handling Test)
result = 10 / 0  # Causes ZeroDivisionError

# No main execution check (Fails Main Execution Check)

# Bad indentation (Fails PEP8 Indentation Test)
def bad_function():
  x = 10  # Should be 4 spaces instead of 2 (Fails PEP8)
return x  # Wrong indentation

# Bad Naming Convention (Fails Naming Conventions Test)
class bad_class:  # Should be PascalCase
    pass

def BadFunction():  # Should be snake_case
    pass

# Use of `eval()` (Fails Security Test)
user_input = "10 + 5"
result = eval(user_input)  # Dangerous use of eval()

# Unnecessary Nested Loops (Fails Performance Test)
for i in range(5):
    for j in range(5):
        for k in range(5):  # Too many nested loops
            print(i, j, k)

# Unused import (Fails Dependency Test)
import math  # This import is not used anywhere

# Logging missing (Fails Logging Test)
print("This is a log message")  # Should use logging.info()

# Improper Exception Handling (Fails Specific Exception Handling Test)
try:
    x = 1 / 0
except:  # No specific exception (should be except ZeroDivisionError)
    print("An error occurred")

# External library used but missing from requirements.txt (Fails Dependency Check)
import pandas as pd  # Should be listed in `requirements.txt`
