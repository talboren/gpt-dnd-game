from typing import List
from models.player import Player
from models.character import Character

class GameEngine:
    def __init__(self, players: List[Player], characters: List[Character]):
        self.players = players
        self.characters = characters
        
    def get_player_by_name(self, name: str) -> Player:
        for player in self.players:
            if player.name == name:
                return player
        return None
    
    def get_character_by_name(self, name: str) -> Character:
        for character in self.characters:
            if character.name == name:
                return character
        return None
    
    def start_game(self):
        print("Welcome to the D&D game!")
        
        # TODO: implement game loop

