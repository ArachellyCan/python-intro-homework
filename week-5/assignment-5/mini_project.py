
#the data to work with form week-5/data/numbers.py
numbers = [4,17,83,5,61,29,74,8,55,93,31,66,14,47,78,3,59,22,86,40]

#Return the smalles number in the list (wiht out using min())
def find_minimum(list):
    smallest = list[0] #start by assuming the first number is the smallest
    for n in list:     #look ate every number in the list
                          
        if n < smallest:  #if this number is samaller that the current smallest
            smallest = n  # then n becomea the new smallest number
    return smallest



#Return the largest number in the list(without using mas())
def find_maximum(list):
    largest = list[0]        #start by assuming the first number is the largest
    for n in list:           #look at every number in the list
                          
        if n > largest:      #if this number is larger than the current largest
            largest = n      # then n becomes the new largest number
    return largest

def linear_search (lst, target):
    for i in range(len(lst)):
        if lst[1] == target:
           return i
    return -1    


#Sort the list from the smallest to the largest using bubble sort

def bubble_sort(lst):
  
    while True:                          # keep making passes until the list is sorted
        swapped = False                  # tracks whether this pass changed anything
        for i in range(len(lst) - 1):    # compare each pair of neighbors (i and i+1)
            if lst[i] > lst[i + 1]:      # if the left number is bigger than the right...
                # ...swap them so the smaller one comes first
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True           # remember that we made a swap
        if not swapped:                  # a full pass with no swaps means it is sorted
            break                        # so stop repeating
    return lst

#main Program (the menu loop)
while True: # repeats forever until hit "break" (option 5)

#show menu
    print("\n===Number Cruncher ===")
    print("1. Find the smallest number")
    print("2. Find the largest number")
    print("3. Sort the list")
    print("4. Display the list")
    print("5. Exit")

 #Ask the user for a choice: .strip() removes accidental spaces
    choice = input("Chose anoption(1-5): ").strip()

    if choice == "1":
    #call the funtion and print that it returns
       print("Minumun:", find_minimum(numbers))

    elif choice == "2":
     print("Maximum:", find_maximum(numbers))

    elif choice == "3":
    #try/except stops the program from crashing from gfashing if the user types letters
        try: 
            target = int(input("Enter a number to search for: "))
        except ValeError:
          print("Please enter a valid integer.")
      # skip the rest and go back to showing the menu
   
        index = linear_search(numbers, target)
        if index != -1:
            print(f"{target} at index {index}. ") 
        else:
            print(f"{target} was not found. ")

    elif choice == "4":
    #Note: this sorts the list itself, so later options use the sorte list
        print("Sorted list:", bubble_sort(numbers))

    elif choice == "5":
        print("Goodbye !")
    break # exits the while loop, which ends the program

else:
    #Anything other than 1-5 ends up here
    print("invalide choice. Please enter a number from 1 to 5.")       

