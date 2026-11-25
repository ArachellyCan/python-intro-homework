# Open the file notes.txt, which is in the data folder.
# '../data/notes.txt' = go up one folder, then into data.
# 'r' = read mode (look, but don't change anything).
# "as file" gives the open file a name: file (a variable).
# "with" closes the file automatically when the block ends.

with open('../data/notes.txt', 'r') as file:

    # Create a variable called line_number and start it at 1.
    # It keeps count of which line we are on.
    # It goes BEFORE the loop so it only starts at 1 once.
    line_number = 1

    # Loop through the file ONE LINE at a time.
    # Each time through, "line" holds the current line.
    for line in file:

        # Print the line with its number.
        # {line.strip()} removes the hidden \n at the end.
        print(f"Line {line_number}: {line.strip()}")

        # Add 1 so the next line gets the next number.
        line_number = line_number + 1
        