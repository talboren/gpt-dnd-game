from models.player import Player
from utils.chatgpt import ChatGPT


class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.rooms = {}
        self.current_room = None
        self.chatgpt = ChatGPT()

    def load_game_world(self, filename):
        # Load game world from file
        pass

    def process_input(self, input_str):
        # Process player input
        pass

    def update_game_state(self):
        # Update game state based on player actions
        pass

    def start_game(self):
        # Start the game loop
        pass
