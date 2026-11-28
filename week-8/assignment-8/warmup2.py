numerator = float(input("Enter the numerator: "))
# 1. Ask for the top number. float() turns the text into a number.

denominator = float(input("Enter the denominator: "))
# 2. Ask for the bottom number, the one you divide by.

try:
    # 3. "Attempt this. It might fail."

    result = numerator / denominator
    # 4. Divide. If the denominator is 0, Python raises ZeroDivisionError
    #    and jumps straight to the except block.

except ZeroDivisionError:
    # 5. Runs ONLY if step 4 tried to divide by zero.

    print("Can't divide by zero — please try a non-zero denominator.")
    # 6. A friendly message instead of a crash.

else:
    # 7. Runs ONLY if the division worked (Page 1: "The else Block").

    print(f"{numerator} ÷ {denominator} = {result}")