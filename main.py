import sports as sports
import time

targeted_team_name = "Toronto Blue Jays"

# i = 0
# old_score = 0
#
# while i = 0:
#     if current_score > old_score:
#         old_score = current_score
#         # send out tweet
#
#     current_score = findTargetScore(getSportsMatches('baseball'), targeted_team_name)
#     time.sleep(30)


def getSportsMatches(target_sport):
    all_sports_matches = sports.all_matches()
    all_targeted_matches = all_sports_matches[target_sport]
    return all_targeted_matches

def findTargetScore(all_targeted_matches, targeted_team_name):
    match_position = []

    for i in range(len(all_targeted_matches)):
        # changes baseball matches to strings and finds all of the targeted teams matches
        all_targeted_matches[i] = str(all_targeted_matches[i])
        if all_targeted_matches[i].find(targeted_team_name) >= 0:
            match_position.append(int(i))

    if match_position == []: # if the team could not be found in input
        return "Team has not yet played today."
    else:
        for n in range(len(match_position)):
            match_temp = all_targeted_matches[match_position[n]]

            # finds whether the targeted team is home or away
            target_home_or_away = match_temp.find(targeted_team_name)
            if target_home_or_away > 0:  # team is away
                target_home_or_away = 1
            else: # team is home
                target_home_or_away = 0

            # parses the game scores
            match_temp = match_temp.split(" ")
            for m in range(len(match_temp)):
                search_temp = match_temp[m]
                search_temp_num = search_temp.find("-")
                if search_temp_num >= 0:
                    current_game_scores = match_temp[m]
                    m = len(match_temp)
            current_game_scores = current_game_scores.split("-")

            # finds the teams score
            target_team_current_score = int(current_game_scores[target_home_or_away])
            return target_team_current_score