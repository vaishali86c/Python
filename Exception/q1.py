# Program to demonstrate exception handling

# Exception handling example with else and finally
try:
    # Ask the user to enter two numbers 
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Try to divide num1 by num2 
    result = num1 / num2

except ValueError:
    print("Please enter valid integers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as e:
    print("An error occurred:", e)

else:
    # This block will be executed if no exception occurs 
    print("Result of division:", result)

finally:
    # This block will always be executed, regardless of whether an exception occurred 
    print("execute the finally block of program..")
