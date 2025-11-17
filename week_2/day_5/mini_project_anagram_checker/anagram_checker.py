import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "sowpods.txt")

class AnagramChecker:
    def __init__(self):
        with open(file_path) as file:
            content = file.read()
            content = content.lower().split()
            self.words = set(content)

    def is_valid_word(self, word):
        return word.lower() in self.words
    
    @staticmethod
    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    
    def get_anagrams(self, word):
        anagrams = []

        for self_word in self.words:
            if AnagramChecker.is_anagram(self_word, word) and self_word != word:
                anagrams.append(self_word)

        return anagrams