
numbers = [1, 2, 3, 4, 5]

def display_menu():
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Sort the list")
    print("6. Reverse the list")
    print("7. Search for an element")
    print("8. Save the list to a file")
    print("9. Load a list from a file")
    print("0. Quit")

while True:
    print("\nCurrent List:", numbers)
    display_menu()
    try:
        option = int(input("Choose an option: "))
        if option == 0:
            print("Exiting the program. Goodbye!")
            break
        elif option == 1: 
            value = int(input("Enter value to append: "))
            numbers.append(value)
            print("Updated List:", numbers)
        elif option == 2:  
            value = int(input("Enter value to insert: "))
            index = int(input("Enter index: "))
            if 0 <= index <= len(numbers):
                numbers.insert(index, value)
                print("Updated List:", numbers)
            else:
                print("Invalid index! Please enter a valid index.")
        elif option == 3: 
            index = int(input("Enter index to pop (leave empty for last element): ") or -1)
            if -len(numbers) <= index < len(numbers):
                popped = numbers.pop(index)
                print(f"Popped element: {popped}")
                print("Updated List:", numbers)
            else:
                print("Invalid index! Please enter a valid index.")
        elif option == 4: 
            value = int(input("Enter value to remove: "))
            if value in numbers:
                numbers.remove(value)
                print("Updated List:", numbers)
            else:
                print("Value not found in the list.")
        elif option == 5:
            numbers.sort()
            print("List sorted:", numbers)
        elif option == 6:  
            numbers.reverse()
            print("List reversed:", numbers)
        elif option == 7: 
            value = int(input("Enter value to search: "))
            if value in numbers:
                print(f"Value {value} found at index {numbers.index(value)}.")
            else:
                print("Value not found in the list.")
        elif option == 8:  
            filename = input("Enter filename to save the list: ")
            with open(filename, "w") as file:
                file.write(",".join(map(str, numbers)))
            print(f"List saved to {filename}.")
        elif option == 9:
            filename = input("Enter filename to load the list from: ")
            try:
                with open(filename, "r") as file:
                    numbers = list(map(int, file.read().strip().split(",")))
                print(f"List loaded from {filename}.")
            except FileNotFoundError:
                print("File not found! Please enter a valid filename.")
            except ValueError:
                print("Invalid file format! Ensure the file contains a comma-separated list of integers.")
        else:
            print("Invalid option! Please choose a valid menu option.")
    except ValueError:
        print("Invalid input! Please enter a number corresponding to the menu options.")
