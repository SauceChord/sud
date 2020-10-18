import unittest

from game import Game, GameError

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.add_room("Spawn") # First added room is where the player start
        self.game.add_room("North of Spawn")
        self.game.add_room("South of Spawn")
        self.game.link_rooms("Spawn", "North of Spawn", "north")
        self.game.link_rooms("Spawn", "South of Spawn", "south")
        self.game.link_rooms("North of Spawn", "Spawn", "south")
        self.game.link_rooms("South of Spawn", "Spawn", "north")

    def test_add_room(self):
        game = Game()
        game.add_room("Spawn")
        self.assertTrue(game.has_room("Spawn"))

    def test_default_player_room(self):
        game = Game()
        self.assertRaises(GameError, game.get_player_room)
        game.add_room("Spawn")
        self.assertInRoom("Spawn")
        game.add_room("Another Room")
        self.assertInRoom("Spawn")

    def test_go_north(self):
        self.game.exec("go north")
        self.assertInRoom("North of Spawn")

    def test_go_south(self):
        self.game.exec("go south")
        self.assertInRoom("South of Spawn")

    def test_go_about(self):
        self.game.exec("go south")
        self.assertInRoom("South of Spawn")
        self.game.exec("go north")
        self.assertInRoom("Spawn")
        self.game.exec("go north")
        self.assertInRoom("North of Spawn")
        self.game.exec("go south")
        self.assertInRoom("Spawn")

    def assertInRoom(self, room):
        self.assertEqual(self.game.get_player_room(), room)
