class Room:
    def __init__(self, description, exits):
        self.description = description
        self.exits = exits
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)

class GameWorld:
    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.player = None

    def add_room(self, room_name, description, exits):
        self.rooms[room_name] = Room(description, exits)

    def set_starting_room(self, room_name):
        self.current_room = self.rooms[room_name]

    def set_player(self, player):
        self.player = player

    def move_player(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.rooms[self.current_room.exits[direction]]
            print(self.current_room.description)
        else:
            print("You can't go that way.")