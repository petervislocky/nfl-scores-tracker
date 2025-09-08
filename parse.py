from typing import List

from extract import GameRow


# TEST: Still being tested, currently returning all statuses not only
# completed games
# TODO: check for Final status and only return those.
def extract_status(games: List[GameRow]) -> List[str]:
    """Returns list of games that have status of completed"""
    completed_games = []
    for game in games:
        completed_games.append(game.get("status", {}))
    return completed_games
