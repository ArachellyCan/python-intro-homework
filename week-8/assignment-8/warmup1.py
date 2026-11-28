while True:
    # 1. Start a loop that repeats until we tell it to stop.

    try:
        # 2. "Attempt this. It might fail."

        number = float(input('Enter a number: '))
        # 3. input() asks the question and waits for you to type.
        #    float() turns the text into a number.
        #    "42" works -> 42.0
        #    "hello" fails -> ValueError -> jumps to except

    except ValueError:
        # 4. Runs ONLY if line 3 failed.

        print("That is not a valid number. Try again. ")
        # 5. Shows the message. The loop then goes back to line 1 and asks again.

    else:
        # 6. Runs ONLY if the try worked, with no error.

        print("You entered:", number)
        # 7. Shows the valid number, like the example: You entered: 42.0

        break
        # 8. Leaves the loop, so the program stops asking.