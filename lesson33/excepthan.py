#number = int(input("Enter a number: "))
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Please enter a valid number.")

try:
    result = 10 / 0
    print(result)
except:
    print("You cannot divide by zero.")

# Exercise
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except:
    print("Invalid input.")

# challenge; the code will ask for Age:, when you input a number it will print the number you inputed directly but when you input a letter or another thing other than number, it will print Invalid age.