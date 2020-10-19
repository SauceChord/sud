class GameError(Exception):
    pass

class Game():
    def __init__(self):
        self.rooms = {}
        self.links = {}
        self.player_room = None

    def add_room(self, room):
        if bool(self.rooms) == False:
            self.player_room = room
        self.rooms[room] = None

    def has_room(self, room):
        return room in self.rooms

    def link_rooms(self, link_from, link_to, direction):
        if link_from not in self.links:
            self.links[link_from] = {}
        self.links[link_from][direction] = link_to

    def go(self, direction):            
        if self.player_room in self.links:
            if direction in self.links[self.player_room]:
                self.player_room = self.links[self.player_room][direction]            

    def exec(self, str):
        substrs = str.split(' ')
        if (substrs[0] == "go"):
            self.go(substrs[1])    
        
    def get_player_room(self):
        if self.player_room == None:
            raise GameError
        return self.player_room