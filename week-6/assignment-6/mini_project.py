
# Number Cruncher - Week 6
# List of numbers to work with
numbers = [4, 17, 83, 5, 61, 29, 74, 8, 55, 93,
           31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


# Function 1: Find the smallest number
def find_min(numbers):
    smallest = numbers[0]

    for n in numbers:
        if n < smallest:
            smallest = n

    return smallest


# Function 2: Find the largest number
def find_max(numbers):
    largest = numbers[0]

    for n in numbers:
        if n > largest:
            largest = n

    return largest


# Function 3: Search for a number using linear search
def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return -1


# Function 4: Sort numbers using bubble sort
def bubble_sort(numbers):
    while True:
        swapped = False

        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:

                # Swap the two numbers
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        if not swapped:
            break

    return numbers


# Function 5: Display the menu
def show_menu():
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")


# Function 6: Run the main program
def main():

    while True:
        show_menu()

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print("Minimum:", find_min(numbers))

        elif choice == "2":
            print("Maximum:", find_max(numbers))

        elif choice == "3":
            try:
                target = int(input("Enter a number to search for: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            index = search(numbers, target)

            if index != -1:
                print(f"{target} found at index {index}.")
            else:
                print(f"{target} was not found.")

        elif choice == "4":
            print("Sorted list:", bubble_sort(numbers))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# Start the program
if __name__ == "__main__":
    main()
