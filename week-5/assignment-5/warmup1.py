total=0                                         # fix 1: starts at 0
for number in range(1,101):                     # correct
    total += number                             # fix 2: add number to total
    print(f"the sum of 1 to 100 is {total}. ")  # fix 3: print the total after the loop