import main_functions

class Elf:
    def __init__(self,level,ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str":11, "dex":12, "con":10,
            "int":16, "wis":14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]

# A) Create an instance of Elf named Elora
Elora = Elf(1)

# B) Create an instance of Elf named Elrond
Elrond = Elf(2,{
            "str":13, "dex": 14, "con": 10,
            "int":18, "wis": 16, "cha":15,
            })
print(Elrond)
# C) Print the value of hp for Elora
print(Elora.hp)

# D) Print the value of hp for Elrond
print(Elrond.hp)

# E) Print the value of level for Elora
print(Elora.level)

# F) Print the value of ability_scores for Elrond
print(Elrond.ability_scores)

# G) Convert the elora object instantiated above into a Python dictionary
#the
EloraD = Elora.__dict__

# H) Printing its type:
print(type(EloraD))

# I) Converting elrond object instantiated above into a Python dictionary
ElrondD = Elrond.__dict__

# J) Printing its type:
print(type(ElrondD))

# K) Printing both Elrond and Elora dictionaries
print(EloraD)
print(ElrondD)

# L) Serializing both Elrond and Elora dictionaries to JSON
#main_functions.save_to_file(EloraD,"Elora.json")
#main_functions.save_to_file(ElrondD,"ElrondD.json")


# M) Deserializing both Elrond and Elora JSON files to Python dictionary
read_Elora = main_functions.read_from_file("Elora.json")
read_Elrond = main_functions.read_from_file("Elrond.json")

# N) Printing their types
print(type(read_Elora))
print(type(read_Elrond))