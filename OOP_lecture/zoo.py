class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo._Zoo__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {zoo.name}: {', '.join(self.mammals)} \nTotal animals: {Zoo._Zoo__animals}"
        elif species == "fish":
            return f"Fishes in {zoo.name}: {', '.join(self.fishes)} \nTotal animals: {Zoo._Zoo__animals}"
        elif species == "bird":
            return f"Birds in {zoo.name}: {', '.join(self.birds)} \nTotal animals: {Zoo._Zoo__animals}"

name = input()
rows = int(input())

zoo = Zoo(name)

for i in range(rows):
    species, name = input().split()
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))
