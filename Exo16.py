
numbers = [1, 2, 3, 4, 5]

while True:
    try:
        index = int(input("Enter index (-1 to quit): "))
        if index == -1:
            break
        if index < 0 or index >= len(numbers):
            print("Invalid index! Please enter a valid index.")
            continue
        new_value = int(input("Enter new value: "))
        numbers[index] = new_value
        print(numbers)
    except ValueError:
        print("Invalid input! Please enter integers only.")
