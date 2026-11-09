names =["Ana","Ben","Cara","Marcus","Zoe"] #index
search=input("Enter a mane to seach for: ")#ask what ever the user types lands in search
found = False #THE BOX found yet? starts as False

for i in range(len(names)):
    if names[i] == search:
        print(f'Found"{search}"at index {i}.')
        found = True
        break

    if not found:
        print(f' "{search}" not found in the List.')