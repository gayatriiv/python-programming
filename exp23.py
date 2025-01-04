try:
    a = 5
    b = 0
    print(a / b)  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("Division by zero error")

print("bye")

try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = a / b
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Invalid input, please enter integers.")
else:
    print(c)
finally:
    print("bye")
