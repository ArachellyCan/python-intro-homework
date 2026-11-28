while True:
    # 1. Start a loop that repeats until we tell it to stop.
    #    "True" is always true, so it would run forever on its own.
    #    Everything indented below belongs to the loop.

    try:
        # 2. "Attempt this. It might fail."

        number = float(input('Enter a number: '))
        # 3. input() shows the question and waits for you to type.
        #    It always gives back TEXT, like "42" or "hello".
        #    float() tries to turn that text into a number.
        #    "42" works -> 42.0
        #    "hello" fails -> Python raises a ValueError
        #    and jumps straight to the except block (line 4).

    except ValueError:
        # 4. Runs ONLY if line 3 raised a ValueError.

        print("That is not a valid number. Try again. ")
        # 5. Shows the friendly message.
        #    The loop reaches the end, goes back to line 1,
        #    and asks again.