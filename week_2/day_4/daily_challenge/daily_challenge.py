import string, re, os

class Text:
    def __init__(self, text):
        self.text = text.lower()

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return f"The word '{word}' was not found."
        return count
    
    def most_common_word(self):
        words = self.text.split()
        freq = {}

        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        if not freq:
            return "No words in text."

        most_common = max(freq, key=freq.get)
        return most_common
    
    def unique_words(self):
        words = self.text.split()
        unique = set(words)
        return list(unique)
    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return cls(content)
    
class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)

    def remove_punctuation(self):
        punctuation = string.punctuation
        cleaned_text = self.text.translate(str.maketrans("", "", punctuation))
        return cleaned_text
    
    def remove_stop_words(self):
        stop_words = {
            "a", "an", "the", "is", "are", "am", "was", "were", "in", "on",
            "at", "to", "of", "for", "and", "or", "that", "this", "it",
            "be", "with", "as", "by", "from"
        }

        words = self.text.split()
        filtered_words = [w for w in words if w.lower() not in stop_words]

        return " ".join(filtered_words)
    
    def remove_special_characters(self):
        cleaned = re.sub(r"[^A-Za-z0-9\s]", "", self.text)
        return cleaned
    
text = Text("Hello world hello")

print(text.word_frequency("hello"))    
print(text.most_common_word())
print(text.unique_words())
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "text.txt")
text_file = Text.from_file(file_path)
print(text_file.text)
cleaner = TextModification("Hello, world! This is great.")
print(cleaner.remove_punctuation())
cleaner = TextModification("This is a simple test for the stop words function.")
print(cleaner.remove_stop_words())
cleaner = TextModification("Hi!! Test@123 works*** yes???")
print(cleaner.remove_special_characters())