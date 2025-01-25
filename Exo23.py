def get_positive_integer():
    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N <= 0:
                print("Please enter a positive integer.")
            else:
                return N
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def print_numbers(N):
    for i in range(-N, N+1):
        if i != 0:
            print(i)

def main():
    N = get_positive_integer()
    print_numbers(N)

if __name__ == "__main__":
    main()
