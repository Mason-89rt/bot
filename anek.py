import json
import random

with open("jokes.json", encoding="utf8") as file:
    data = json.load(file)
    print(random.choice('jokes'))
    anek = random.choice(data["jokes"])
    anek1 = random.choice(data["joke"])
    anek2 = random.choice(data["jok"])
    print(anek,anek1,anek2)