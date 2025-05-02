import math 
n = int(input("Enter a number: "))

if n >= 0:
    square_root = math.sqrt(n)
else:
    square_root = "Undefined (square root of negative number)"

if n > 0:
    natural_log = math.log(n)
else:
    natural_log = "Undefined (log of non-positive number)"


sine_value = math.sin(n)

print(f"Suare root: {square_root}")
print(f"Natural log: {natural_log}")
print(f"sine: {sine_value}")