age = int(input("Enter your age : "))

# 1. Check for invalid input first
if age < 1 or age > 150:
    print("Enter valid Value from 1 - 150")

# 2. Handle adults
elif age >= 18:
    print("You can drive")

# 3. Handle minors (age is valid, but less than 18)
else:
    print("You cannot drive")

    # Nested if to provide extra detail for those 15 and under
    if age <= 15:
        print("Cannot even apply for driving licence")

print("End of code")
