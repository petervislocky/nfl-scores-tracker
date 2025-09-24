from __future__ import annotations
from typing import Any, TypedDict
import requests


class GameRow(TypedDict):
    away_abbr: str
    home_abbr: str
    away_score: int
    home_score: int
    status: str


def make_api_request(url: str) -> dict[str, Any]:
    response = requests.get(url)
    response.raise_for_status()
    try:
        return response.json()
    except ValueError:
        raise RuntimeError("Expected JSON but recieved something else")


def extract_api_data(payload: dict[str, Any]) -> list[GameRow]:
    """
    Takes decoded JSON and returns a list of `GameRow` dicts.

    Extracts and stores relevant data defined above in `GameRow`.
    """
    games: list[GameRow] = []
    for event in payload.get("events", []):
        comps = event.get("competitions") or []
        if not comps:
            continue
        comp = comps[0]

        teams = comp.get("competitors") or []
        if len(teams) < 2:
            continue

        # ensure order: index 0 = away, index 1 = home
        teams.sort(key=lambda t: t.get("homeAway") != "away")
        away, home = teams

        status = (
            comp.get("status", {}).get("type", {}).get("shortDetail")
            or comp.get("status", {}).get("type", {}).get("detail")
            or ""
        )

        games.append(
            {
                "away_abbr": away.get("team", {}).get("abbreviation", ""),
                "home_abbr": home.get("team", {}).get("abbreviation", ""),
                "away_score": int(away.get("score") or 0),
                "home_score": int(home.get("score") or 0),
                "status": status,
            }
        )
    return games
