
from functions.run_python_file import run_python_file

print("Test 1: run_python_file('calculator', 'main.py')")
print(run_python_file("calculator", "main.py"))

print("\nTest 2: run_python_file('calculator', 'main.py', ['3 + 5'])")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("\nTest 3: run_python_file('calculator', 'tests.py')")
print(run_python_file("calculator", "tests.py"))

print("\nTest 4: run_python_file('calculator', '../main.py')")
print(run_python_file("calculator", "../main.py"))

print("\nTest 5: run_python_file('calculator', 'nonexistent.py')")
print(run_python_file("calculator", "nonexistent.py"))

