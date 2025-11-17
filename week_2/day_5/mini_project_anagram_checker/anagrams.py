from anagram_checker import AnagramChecker

checker = AnagramChecker()

while True:
    print("1. Check a word for anagrams")
    print("2. Exit")
    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        word = input("Enter a word to check: ").strip()

        if not word.isalpha():
            print("Invalid input! Only letters are allowed.")
            continue

        valid = checker.is_valid_word(word)
        anagrams = checker.get_anagrams(word)

        print(f"\nWord: {word}")
        print(f"Valid word: {'Yes' if valid else 'No'}")
        print(f"Anagrams found ({len(anagrams)}): {', '.join(anagrams) if anagrams else 'None'}")

    elif choice == "2":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")