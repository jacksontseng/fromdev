from basketball_info import game_dictionary

# This method returns the team's status
def home_or_away(team_name):
  return game_dictionary[team_name]['status']


# Write a new method that returns a team's colors
def team_colors(team_name):
    list = game_dictionary[team_name]['team_colors']
    return str(list[0]) + " and " + str(list[1])

#Write a method that returns a string listing every player and their respective points
def player_points(team_name):
    name = game_dictionary[team_name]['players']
    points = game_dictionary[team_name]['players']
    result = ''
    for player in "length of array":
        game_dictionary[team_name]['players'][player]['name']




#This method should return all of the statistics for a player, given that players team and name
def player_stats(team, player_name):
    pass

# Return a player's shoe size.
def shoe_size(team, player_name):
    pass

# Find the player on the team with the biggest shoe size and return their steals for the game
def big_shoe_stealer(team):
    pass
print player_points('Brooklyn Nets')
