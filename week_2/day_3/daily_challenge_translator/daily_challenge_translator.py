import googletrans

translator = googletrans.Translator()

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

french_to_english = {}
for word in french_words:
    french_to_english[word] = translator.translate(word, dest = 'en').text

print(french_to_english)