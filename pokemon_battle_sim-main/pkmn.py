import json

from backend.classes.stats import Stats
from backend.classes.move import Move

class Pokemon():

    # Allows the Pokemon to take damage
    def takeDmg(self, dmg:int):
        self.curr_hp = max(0, self.curr_hp - int(dmg))

    # Initialises the Pokemon class from a jso n file
    ### THIS FUNCTION IS FOR YOU TO COMPLETE ###
    def __init__(self, pkmnInfo: json) -> None:

        ### POKEMON CHECKING ###

        # ----Your code here---- #
        assert(len(pkmnInfo["types"]) <=2)
        assert(pkmnInfo["stats"]["hp"] <=100)
        assert(len(pkmnInfo["moves"]) <=4)
        assert(pkmnInfo["stats"]["attack"] <=60)
        assert(pkmnInfo["stats"]["special attack"] <=100)
        assert(pkmnInfo["stats"]["defence"] <=50)
        assert(pkmnInfo["stats"]["special defence"] <=50)
        assert(pkmnInfo["stats"]["speed"] <=100)
        for move in pkmnInfo["moves"]:
            assert(move["power"]<=100)
            assert(move["accuracy"]<=100)
        # meow
        
        

        ### STANDARD FIELDS ### (Populating the blank Pokemon card)
        self.pokemon = pkmnInfo['pokemon']
        self.nickname = pkmnInfo['nickname']
        self.trainer= pkmnInfo['trainer']
        # ----Your code here---- #




        ### SPECIAL FIELDS ### 
        
        # Stats object will help us handle and process the data
        # (Fill in the blank)
        self.stats = Stats(pkmnInfo["stats"])

        # Initialise a list of moves that your pokemon can make (think about Python lists)
        self.moves = []
        # For each move in the JSON file use the JSON to form a move object and append it in
        for move_json in pkmnInfo['moves']:
            move = Move(move_json)
            self.moves.append(move)


        # ----Your code here---- #
    
