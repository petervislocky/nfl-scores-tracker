from __future__ import annotations

from .extract import GameRow


def extract_completed_games(games: list[GameRow]) -> list[GameRow]:
    """Returns list of games that have status of completed"""
    completed_games = []
    for game in games:
        if game["status"] == "Final":
            completed_games.append(game)
    return completed_games


def extract_winner(completed_games: list[GameRow]) -> list[str]:
    """Parses list of completed games and returns the abbreviation of the winning team"""
    todays_winners = []
    for game in completed_games:
        away_abbr, home_abbr = game.get("away_abbr", ""), game.get("home_abbr", "")
        away_score, home_score = game.get("away_score", ""), game.get("home_score", "")
        if home_score > away_score:
            todays_winners.append(home_abbr)
        else:
            todays_winners.append(away_abbr)
    return todays_winners
