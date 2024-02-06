def swap_numbers(a, b):
    # XOR swap algorithm
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a, b

# Take user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Perform the swap
num1, num2 = swap_numbers(num1, num2)

print(f"After swapping: num1 = {num1}, num2 = {num2}")

