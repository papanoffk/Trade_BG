import orjson
from card import Card
from PIL import Image

class FileManager():
    def __init__(self, set):
        self.Cards = {set : self.Loads_cards(set)} # 1) tech 2) ...

    def Dumps_cards(self, set):
        with open(f'{set}.json', "wb") as file:
            cards = []
            for card in self.Cards[set]:
                cards.append(card['card'])
            file.write(orjson.dumps(cards))
            print("Dumps good.")

    def Loads_cards(self, set) -> list:
        with open(f'{set}.json', "rb") as file:
            new_card = []
            card_img = []
            for card in orjson.loads(file.read()):
                num = card['Number_in_realese']
                img = Image.open(f'image/{set}/bers ({num}).jpg')
                img.resize((63, 89))
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
                                    Text_card = card['Text_card']), 'image' : img})
            return new_card

    def __del__(self):
        self.Dumps_cards('tech')
