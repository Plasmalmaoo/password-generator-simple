import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Choose which types of characters to include
upper, lower, nums, syms = True, True, True, True

# Build the character set
all_chars = ""
if upper:
    all_chars += upper_case
if lower:
    all_chars += lower_case
if nums:
    all_chars += numbers
if syms:
    all_chars += symbols

print("=== Password Generator ===")

while True:
    try:
        length = int(input("Enter password length: "))
        amount = int(input("Enter number of passwords to generate: "))
        break
    except ValueError:
        print("Please enter a valid number.")

for _ in range(amount):
    password = "".join(random.sample(all_chars, length))
    print(password)

input("\nProgram finished. Press Enter to exit...")