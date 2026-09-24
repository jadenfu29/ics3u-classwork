#The name of the team
team = "Toronto Blue Jays"
#the current date
current_date = "July 18, 2021"
#This is the player we are talking about
player = "Vladimir Guerrero Jr."
#The integer number of homeruns he has had
home_runs_to_date = 31
#The integer number of games he has played
games_played = 88
#Total number of season games that he has played
total_season_games = 162
#His home run record
home_run_record = 73

games_remaining = total_season_games - games_played
home_runs_per_game = home_runs_to_date / games_played
projected_home_runs = home_runs_per_game * total_season_games
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {round(home_runs_per_game,2)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs)} home runs this season.")