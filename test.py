import orjson

from card import Card
from FileManager import FileManager as fm

FM = fm()

def default(obj):
    if isinstance(obj, Card):
        return obj.To_json()
cards = []

for i in range(1,100):
    cards.append(Card(Number_in_realese = i))

with open("tech.json", "wb") as file:
    file.write(orjson.dumps(cards))

for card in FM.Cards:
    print(card)
