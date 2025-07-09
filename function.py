#Create a function called divide(a, b) that returns the result of a / b.
# Use try...except to handle divide-by-zero errors and display a user-friendly message.
def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "division by zero is not possible, please try again."
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(div(a,b))