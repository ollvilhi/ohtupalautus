from player_reader import PlayerReader



class StatisticsService:
    """Palvelun tarjoava luokka. Tarjoaa metodit yhden pelaajan tietojen
    näyttämiseen, pistepörssin näyttämiseen ja yhden joukkueen pelaajien
    tietojen näyttämiseen."""

    def __init__(self, plr): # (self):
        self._plr = plr
        self._players = plr.get_players() # reader.get_players()

    def search(self, name):
        for self._plr in self._players:
            if name in self._plr.name:
                return self._plr
        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda _plr: _plr.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(_plr):
            return _plr.points

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
