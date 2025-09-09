from typing import List

from extract import GameRow


def extract_completed_games(games: List[GameRow]) -> List[str]:
    """Returns list of games that have status of completed"""
    completed_games = []
    for game in games:
        if game["status"] == "Final":
            completed_games.append(game)
    return completed_games


# TODO: write a method to pull the winners from the final games
