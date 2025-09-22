import extract
import parse

BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"


def main():
    api_response = extract.make_api_request(BASE_URL)
    games = extract.extract_api_data(api_response)
    # print(games)
    completed_games = parse.extract_completed_games(games)
    # print(completed_games)
    winners = parse.extract_winner(completed_games)
    print(winners)


if __name__ == "__main__":
    main()
