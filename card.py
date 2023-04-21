import dataclasses

@dataclasses.dataclass
class Card:
    Number_in_collection: int = 0

    #discription
    Release: int = 1
    Number_in_realese: int = 1
    Type_card: str = 'creature' # creature. spell, help, hero
    Color: list[int] = dataclasses.field(default_factory=lambda: [0,0,0,0]) # стипи, горы, лес, болота, тьма
    Name: str = 'name'
    Cost: int = 0
    Attack: int = None
    Hit: int = None
    Class_card: str = 'class'
    Text_card: str = 'text'
