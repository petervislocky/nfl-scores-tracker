import extract
import parse

BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"


def main():
    api_response = extract.make_api_request(BASE_URL)
    games = extract.extract_api_data(api_response)
    games_status = parse.extract_status(games)
    print(games_status)


if __name__ == "__main__":
    main()
