# Create a function that checks if a score is valid
def is_valid_score(score):

    # Check if the score is between 0 and 100
    if score >= 0 and score <= 100:

        # Send True back to the code that called the function
        return True

    else:

        # Send False back to the code that called the function
        return False


# Ask the user to enter a score
score = int(input("Enter a score: "))

# Call the function and give it the score
# If the function returns True, run this block
if is_valid_score(score):

    # Print this if the score is valid
    print("Valid score.")

else:

    # Print this if the score is not valid
    print("Invalid score — must be between 0 and 100.")