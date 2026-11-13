

# Number Cruncher - Week 6
# This program allows the user to find the minimum,
# maximum, search for a number, and sort a list.


# List of numbers to work with
numbers = [4, 17, 83, 5, 61, 29, 74, 8, 55, 93,
           31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


# Function 1: Find the smallest number
def find_min(numbers):

    # Start by assuming the first number is the smallest
    smallest = numbers[0]

    # Loop through every number in the list
    for n in numbers:

        # Check if the current number is smaller
        if n < smallest:

            # Update smallest with the new smaller number
            smallest = n

    # Return the smallest number found
    return smallest


# Function 2: Find the largest number
def find_max(numbers):

    # Start by assuming the first number is the largest
    largest = numbers[0]

    # Loop through every number in the list
    for n in numbers:

        # Check if the current number is larger
        if n > largest:

            # Update largest with the new larger number
            largest = n

    # Return the largest number found
    return largest


# Function 3: Search for a number using linear search
def search(numbers, target):

    # Loop through the list using index positions
    for i in range(len(numbers)):

        # Compare the current list value with the target
        if numbers[i] == target:

            # Return the index where the number was found
            return i

    # Return -1 if the number is not found
    return -1


# Function 4: Sort numbers using bubble sort
def bubble_sort(numbers):

    # Create a copy so the original list is not changed
    sorted_numbers = numbers.copy()

    # Keep repeating the sorting process until no swaps are needed
    while True:

        # Assume no numbers need to be swapped
        swapped = False

        # Compare each number with the number next to it
        for i in range(len(sorted_numbers) - 1):

            # Check if the current number is greater than the next number
            if sorted_numbers[i] > sorted_numbers[i + 1]:

                # Swap the two numbers to put them in the correct order
                sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1], sorted_numbers[i]

                # Record that a swap happened
                swapped = True

        # If no swaps happened, the list is already sorted
        if not swapped:
            break

    # Return the new sorted list without changing the original
    return sorted_numbers


# Function 5: Display the menu
def show_menu():

    # Display the program title and available options
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")


# Function 6: Run the main program
def main():

    # Keep displaying the menu until the user chooses to quit
    while True:

        # Call the function that displays the menu
        show_menu()

        # Ask the user to select an option
        choice = input("Choose an option (1-5): ").strip()

        # Option 1: Find and display the smallest number
        if choice == "1":
            print("Minimum:", find_min(numbers))

        # Option 2: Find and display the largest number
        elif choice == "2":
            print("Maximum:", find_max(numbers))

        # Option 3: Search for a number
        elif choice == "3":

            # Use try/except to handle invalid input
            try:
                # Ask the user for a number and convert it to an integer
                target = int(input("Enter a number to search for: "))

            # Handle the error if the user does not enter an integer
            except ValueError:
                print("Please enter a valid integer.")

                # Return to the menu
                continue

            # Call the search function and save the returned index
            index = search(numbers, target)

            # Check if the number was found
            if index != -1:
                print(f"{target} found at index {index}.")

            # Display a message if the number was not found
            else:
                print(f"{target} was not found.")

        # Option 4: Sort and display the numbers
        elif choice == "4":
            print("Sorted list:", bubble_sort(numbers))

        # Option 5: Exit the program
        elif choice == "5":
            print("Goodbye!")

            # Stop the while loop
            break

        # Handle an invalid menu selection
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# Start the program
# This checks that the file is being run directly
if __name__ == "__main__":

    # Call the main function to start the program
    main()