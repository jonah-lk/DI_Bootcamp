import random, os

def get_words_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
            return words
    except FileNotFoundError:
        print("Word list file not found.")
        return []

def get_random_sentence(length):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "words.txt")
    words = get_words_from_file(file_path)

    if not words:
        return "No words available."

    sentence_words = [random.choice(words) for _ in range(length)]
    sentence = " ".join(sentence_words).lower()
    return sentence

def main():
    print("This program generates a random sentence.")
    print("You can choose a sentence length between 2 and 20 words.")

    user_input = input("Enter sentence length: ")

    try:
        length = int(user_input)
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    if not 2 <= length <= 20:
        print("Error: Number must be between 2 and 20.")
        return

    sentence = get_random_sentence(length)
    print("\nGenerated sentence:")
    print(sentence)

main()