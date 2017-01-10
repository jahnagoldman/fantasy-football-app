import urllib.parse
import urllib.request
import urllib.response
import json


def get_player_data():
    userName = "mhmcdonald"
    passWord = "uofc2017"
    top_level_url = "https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/daily_player_stats.json?fordate=20161120"
    date = top_level_url[-6:]

    # create an authorization handler
    p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, top_level_url, userName, passWord);

    auth_handler = urllib.request.HTTPBasicAuthHandler(p)

    opener = urllib.request.build_opener(auth_handler)

    urllib.request.install_opener(opener)

    try:
        result = opener.open(top_level_url)
        messages = result.read()
        matches = json.loads(messages.decode("utf-8"))
        stats = matches["dailyplayerstats"]
        player_stats = stats["playerstatsentry"]
        # print(player_stats)

        ## player_stats is a list of dictionaries
        parsed_data = []
        for dict in player_stats:
            player_info = dict["player"]
            player_statistics = dict["stats"]
            player_id = player_info["ID"]
            player_last_name = player_info["LastName"]
            position = player_info["Position"]
            if position == "C":
                continue

            playerstats = {}
            for stat in player_statistics:
                playerstats['name'] = player_last_name
                playerstats['player_id'] = player_id
                playerstats['date'] = date
                playerstats['stat'] = stat
                playerstats['amount'] = player_statistics[stat]["#text"]
                parsed_data.append(playerstats)
        return parsed_data
    except IOError as e:
        print(e)