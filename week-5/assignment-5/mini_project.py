
# The data to work with from week-5/data/numbers.py
numbers = [4,17,83,5,61,29,74,8,55,93,31,66,14,47,78,3,59,22,86,40]

# Return the smallest number in the list (without using min())
def find_minimum(lst):
    smallest = lst[0]    # start by assuming the first number is the smallest
    for n in lst:        # look at every number in the list
        if n < smallest: # if this number is smaller than the current smallest
            smallest = n  # then n becomes the new smallest number
    return smallest

# Return the largest number in the list (without using max())
def find_maximum(lst):
    largest = lst[0]       # start by assuming the first number is the largest
    for n in lst:          # look at every number in the list
        if n > largest:    # if this number is larger than the current largest
            largest = n    # then n becomes the new largest number
    return largest

# Return the index of target in the list, or -1 if it is not found
def linear_search(lst, target):
    for i in range(len(lst)):      # i is the index of each item, one at a time
        if lst[i] == target:       # compare the item at index i (not a fixed index) 
            return i               # found it, so return its index
    return -1                      # the loop finished without a match


# Sort the list from the smallest to the largest using bubble sort
def bubble_sort(lst):
    while True:                                         # keep making passes until the list is sorted
        swapped = False                                 # tracks whether this pass changed anything
        for i in range(len(lst) - 1):                   # compare each pair of neighbors (i and i+1) 
            if lst[i] > lst[i + 1]:                     # compare each pair of neighbors (i and i+1)
                
                # ...swap them so the smaller one comes first
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True                          # remember that we made a swap
        if not swapped:                                 # a full pass with no swaps means it is sorted
            break                                       # so stop repeating
    return lst


# Main program (the menu loop)
while True:
    
    # Show the menu 
    print("\n=== Number Cruncher ===")
    print("1. Find the smallest number")
    print("2. Find the largest number")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Exit")


    # Ask the user for a choice: .strip() removes accidental spaces
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        print("Minimum:", find_minimum(numbers))

    elif choice == "2":
        print("Maximum:", find_maximum(numbers))

    elif choice == "3":

        # try/except stops the program from crashing if the user types letters
        try:
            target = int(input("Enter a number to search for: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        index = linear_search(numbers, target)
        if index != -1:
            print(f"{target} at index {index}.")
        else:
            print(f"{target} was not found.")

    elif choice == "4":
        # Note: this sorts the list itself, so later options use the sorted list
        print("Sorted list:", bubble_sort(numbers))

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        # Anything other than 1-5 ends up here
        print("Invalid choice. Please enter a number from 1 to 5.")
