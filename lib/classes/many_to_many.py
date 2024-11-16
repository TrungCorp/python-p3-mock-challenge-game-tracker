class Game:
    def __init__(self, title):
        if not isinstance(title,str) or len(title) == 0:
            raise ValueError("Title must be non-empty string")
        self._title = title

    @property
    def title(self):
        return self._title
        
    def results(self):
        return [result for result in Result._all_results if result.game == self]

    def players(self):
        return list(set(result.player for result in self.results()))

    def average_score(self, player):
        player_results = [result.score for result in self.results() if result.player == player]

        if player_results:
            return sum(player_results) / len(player_results)
        return 0.0

class Player:
    def __init__(self, username):
        if not isinstance(username,str) or not (2<=len(username) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters")
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str) or not (2 <= len(new_username) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters")
        self._username = new_username

    def results(self):
        return [result for result in Result._all_results if result.player == self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        return any(result.game == game for result in self.results())

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)

class Result:
    all = []
    _all_results = []
    def __init__(self, player, game, score):
        if not isinstance(player, Player) or not isinstance(game, Game):
            raise ValueError("Result must be initialized with a Player and a Game")
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("Score must be an integer between 1 and 5000")
        self._player = player
        self._game = game
        self._score = score
        Result._all_results.append(self)
        Result.all.append(self)

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score
       