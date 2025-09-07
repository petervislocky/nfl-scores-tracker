import espn_api

BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"


def main():
    api_response = espn_api.make_api_request(BASE_URL)
    print(espn_api.extract_scores(api_response))


if __name__ == "__main__":
    main()
