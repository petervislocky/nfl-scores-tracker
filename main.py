from __future__ import annotations

from api import extract
from api import parse

API_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"


def main() -> None:
    api_response = extract.make_api_request(API_URL)
    games = extract.extract_api_data(api_response)
    # print(games)
    completed_games = parse.extract_completed_games(games)
    # print(completed_games)
    winners = parse.extract_winner(completed_games)
    print("===TODAYS WINNERS===")
    print(*winners, sep="\n")


if __name__ == "__main__":
    main()
