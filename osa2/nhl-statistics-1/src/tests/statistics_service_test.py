import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.points, 37 + 53)

    def test_search_none(self): 
        # TODO
        #player = self.stats.search(None)
        #self.assertEqual(player.name, None)
        pass

    def test_team_player_list(self):
        players_of_team = self.stats.team("EDM")
        self.assertEqual(players_of_team, list(players_of_team))

    def test_top_players(self):
        top = self.stats.top(2)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")