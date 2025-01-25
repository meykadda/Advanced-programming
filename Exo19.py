
unique_words = set()

def display_unique_words():
    print("\nUnique Words (Alphabetically):")
    print(", ".join(sorted(unique_words)))

while True:
    word = input("Enter a word: ").strip()  
    if word in unique_words:
        print(f"\nYou typed in {len(unique_words)} unique words.")
        display_unique_words()
        save_option = input("Would you like to save the unique words to a file? (yes/no): ").strip().lower()
        if save_option == "yes":
            filename = input("Enter filename to save the words: ").strip()
            with open(filename, "w") as file:
                file.write("\n".join(sorted(unique_words)))
            print(f"Unique words saved to {filename}.")
        print("Goodbye!")
        break
    else:
        unique_words.add(word)
        print(f"Added: {word}")
