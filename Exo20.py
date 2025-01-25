import os

def display_statistics(lst):
    if not lst:
        print("Statistics: List is empty.")
        return

    mean = sum(lst) / len(lst)
    median = lst[len(lst) // 2] if len(lst) % 2 != 0 else (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2

    print(f"Statistics: Mean = {mean:.2f}, Median = {median:.2f}")

def save_list_to_file(lst):
    filename = input("Enter the filename to save the list: ").strip()
    with open(filename, "w") as file:
        file.write(",".join(map(str, lst)))
    print(f"List saved to {filename}")

def load_list_from_file():
    filename = input("Enter the filename to load the list: ").strip()
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()
            return list(map(int, content.split(",")))
    else:
        print("File not found.")
        return []

def main():
    user_list = []
    print("Welcome to the Sorted List Builder!")
    if input("Do you want to load an existing list? (yes/no): ").strip().lower() == "yes":
        user_list = load_list_from_file()

    while True:
        user_input = input("Enter a number (or 0 to exit): ")

        try:
            number = int(user_input)
            if number == 0:
                break
            user_list.append(number)
            print(f"Current List: {user_list}")
            print(f"Sorted List (Ascending): {sorted(user_list)}")
            print(f"Sorted List (Descending): {sorted(user_list, reverse=True)}")
            display_statistics(sorted(user_list))
        except ValueError:
            print("Invalid input. Please enter an integer.")
    if input("Do you want to save the list to a file? (yes/no): ").strip().lower() == "yes":
        save_list_to_file(user_list)

    print("Thank you for using the Sorted List Builder!")

if __name__ == "__main__":
    main()
