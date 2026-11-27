import csv
# csv -> Python's tool for reading CSV files (gives us csv.DictReader)

import sys
# sys -> lets us stop the program early with sys.exit()

# ---- 1. Containers that hold our results ----
good_rows = []
# An empty list. Each clean row goes in here as a dictionary.

skipped = []
# An empty list. For each bad row we store a message saying why it was skipped.

attempted = 0
# A counter. It goes up by 1 for every row we try, good or bad.

# ---- 2. Open the file safely ----
try:
    # "Attempt this. The file might not exist."

    with open("../data/messy_data.csv", "r", newline="") as f:
        # Open the data file in read-only mode ("r"), so it is never changed.
        # The open file gets the nickname f.

        reader = csv.DictReader(f)
        # Reads the first line (name,category,amount) as the labels,
        # then hands us every other line as a dictionary.

        # ---- 3. Go through the rows one at a time ----
        for row_number, row in enumerate(reader, start=1):
            # enumerate counts the rows for us, starting at 1.
            # row_number = 1, 2, 3...   row = that row's dictionary

            attempted += 1
            # Add 1 to the counter for every row we look at.

            # ---- 4. Guard: extra columns ----
            if None in row:
                # DictReader stores extra values under a None key,
                # so None being in the row means it has too many columns.
                # (This is Hint 2. It's an if, not a try/except, because
                # no error is raised.)

                skipped.append(f"Row {row_number}: extra column detected — skipped")
                # Write down which row and why.

                continue
                # Jump straight to the next row. The code below is skipped
                # for this one.

            # ---- 5. Try to turn the amount into a number ----
            try:
                amount = float(row["amount"])
                # row["amount"] finds the amount by its label.
                # float() turns the text into a number.
                # ValueError -> if the text is empty ('') or words ('fifteen')
                # KeyError   -> if the "amount" column doesn't exist at all

                good_rows.append({
                    "name": row["name"],
                    "category": row["category"],
                    "amount": amount,
                })
                # It worked, so save this row in our clean list.
                # The amount is now a real number, not text.

            except ValueError:
                # Runs when float() can't convert the text.
                skipped.append(
                    f"Row {row_number}: ValueError — could not convert '{row['amount']}' to float"
                )
                # Records the row number and the bad value that caused it.

            except KeyError as e:
                # Runs if a column is missing. With this data it may never
                # happen, but the assignment asks us to include it.
                skipped.append(f"Row {row_number}: KeyError — missing column {e}")
                # e holds the name of the missing column.

except FileNotFoundError:
    # Runs ONLY if the data file can't be found.
    print('Error: "messy_data.csv" was not found. Please check the file path.')
    sys.exit()
    # Stop the program here, as the assignment says.

# ---- 6. Print the report ----
print("=== CSV Report ===")
print(f"Rows attempted:  {attempted:>2}")
# {attempted:>2} -> show the number right-aligned in 2 spaces

print(f"Rows parsed:     {len(good_rows):>2}")
# len(good_rows) -> how many rows are in the clean list

print(f"Rows skipped:    {len(skipped):>2}")
# len(skipped) -> how many bad rows we recorded

print()
# A blank line, to space out the report.

print("Skipped rows:")
for message in skipped:
    print(f"  {message}")
    # Prints each skipped-row message we saved earlier.

print()

print("Clean data:")
for r in good_rows:
    print(f"  {r['name']} | {r['category']} | ${r['amount']:.2f}")
    # {r['amount']:.2f} -> show the amount with exactly 2 decimal places