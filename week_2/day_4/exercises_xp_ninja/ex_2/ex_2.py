import random, json, os

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.stats = self.generate_stats()

    def generate_stats(self):
        abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        stats = {}
        for ability in abilities:
            rolls = [random.randint(1, 6) for _ in range(4)]
            rolls.remove(min(rolls))
            stats[ability] = sum(rolls)
        return stats

class Game:
    def __init__(self):
        self.characters = []

    def create_characters(self, n_players):
        for i in range(n_players):
            print(f"\nCreating character for Player {i+1}")
            name = input("Enter character's name: ")
            age = int(input("Enter character's age: "))
            char = Character(name, age)
            self.characters.append(char)

    def export_json(self, filename):
        data = []
        for char in self.characters:
            data.append({
                "name": char.name,
                "age": char.age,
                "stats": char.stats
            })
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Characters exported to {filename}")

    def export_txt(self, filename):
        with open(filename, "w") as f:
            for char in self.characters:
                f.write(f"Name: {char.name}, Age: {char.age}\n")
                for stat, value in char.stats.items():
                    f.write(f"{stat}: {value}\n")
                f.write("\n")
        print(f"Characters exported to {filename}")

def main():
    print("Welcome to Dungeons & Dragons Character Generator!")
    n_players = int(input("How many players are playing? "))
    
    game = Game()
    game.create_characters(n_players)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "characters.json")
    game.export_json(file_path)
    file_path = os.path.join(base_dir, "characters.txt")
    game.export_txt(file_path)
    print("\nAll characters have been generated and saved!")

if __name__ == "__main__":
    main()