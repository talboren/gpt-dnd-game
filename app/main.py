from fastapi import FastAPI

from utils.chatgpt import ChatGPT
from models.player import Player
from models.character import Character

app = FastAPI()

chatbot = ChatGPT()

game_sessions = {}

@app.post("/game")
async def new_game(player_id: str):
    player = Player(player_id)
    character = Character()
    game_sessions[player_id] = {"player": player, "character": character}
    return {"message": "New game session created."}

@app.post("/game/{player_id}")
async def game_input(player_id: str, input_text: str):
    game_session = game_sessions[player_id]
    character = game_session["character"]
    response = chatbot.generate_response(input_text, character.state)
    character.update_state(response)
    return {"message": response}

