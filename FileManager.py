import orjson
from card import Card
from PIL import Image

class FileManager():
    def __init__(self):
        self.Cards = {'tech' : self.Loads_cards('tech')}

    def Dumps_cards(self, filename, cards):
        with open(filename, "wb") as file:
            file.write(orjson.dumps(cards))
            print("Dumps good.")

    def Loads_cards(self, set) -> list:
        with open(f'{set}.json', "rb") as file:
            new_card = []
            card_img = []
            for card in orjson.loads(file.read()):
                num = card['Number_in_realese']
                s = 2
                new_card.append({'card' : Card(Number_in_collection = card['Number_in_collection'],
                                    Release = card['Release'],
                                    Number_in_realese = card['Number_in_realese'],
                                    Type_card = card['Type_card'],
                                    Color = card['Color'],
                                    Name = card['Name'],
                                    Cost = card['Cost'],
                                    Attack = card['Attack'],
                                    Hit = card['Hit'],
                                    Class_card = card['Class_card'],
                                    Text_card = card['Text_card']), 'image' : Image.open(f'image/{set}/bers ({num}).jpg')})
            return new_card
