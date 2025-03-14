from constants import PLAYERS, TEAMS  

#Clean the height, experience and guardian fields
def clean_data(data): 
    cleaned = []
    for user in data: 
        fixed = {}
        fixed["name"] = user["name"]
        # Split guardian string into a list and remove the "and" between names
        fixed["guardian"] = user["guardians"].split("and")
        if user["experience"] == 'YES':
            fixed["experience"] = True
        else:
            fixed["experience"] = False   
        fixed["height"] = int(user["height"])
        cleaned.append(fixed)
    return cleaned 

# print(clean_data(data))

#Create teams with a balanced number of players and player experience 
def balance_teams(teams,players):

    #Placeholders for inexperienced and experienced players 
        experienced_players = []
        inexperienced_players = []

    # Divide players into experienced and inexperienced groups
        for player in PLAYERS: 
            if player['experience'] == True:
                experienced_players.append(PLAYERS)
            else:
                inexperienced_players.append(PLAYERS)
 
    # Distribute inexperienced and experienced players evenly amongst the teams
    num_players_team = len(players) / len(teams)
    experienced_teams = int(len(experienced_players)/len(TEAMS))
    inexperienced_teams = int(len(inexperienced_players)/len(TEAMS))
     
     # Loop through the teams to assign players 

     balanced_teams = {
         team: {
             "experienced": [],
             "inexperienced": [],
             "total_experienced": 0,
             "total_inexperienced": 0, 
             average_height: 0
             } for teams in teams 
      }
            
for team in TEAMS: 
    for _in range(experienced_teams):
        player = experienced_players.pop()
        teams_assignment[team]["players"].append(player)
        teams_assignment[team]["experience"]+= 1

for team in TEAMS: 
    for _ in range(inexperienced_teams):
        player = inexperienced_players.pop()
        teams_assignment[team]["players"].append(player)
        teams_assignment[team]["inexperience"] += 1


#Calculate average height of current team being looped

def avg_player_heights(team):
    player_heights = []
    for player in team:
        height = player["height"]
        player_heights.append(height)
    avg_height = sum(player_heights) / len(player_heights)
return round(avg_height, 1)

    teams_assignment[team]["avg_height"] = avg_player_heights(teams_assignment[team]["players"])

    # Assign a variable to each team

    team1 = teams_assignment[TEAMS[0]]
    team2 = teams_assignment[TEAMS[1]]
    team3 = teams_assignment[TEAMS[2]]

#Starting Menu for Users
def menu_stats_tool():
    selection = input(" BASKETBALL TEAM STATS TOOL\n\n ======MENU=====:\n-> A: Display Team Stats \n-> B: Quit"
    )
    if selection.upper() == "A":
        choice = input("\nEnter an option: \n A) Panthers \n B) Bandits \n C) Warriors ")
        if choice == "A"
            print(f"\nTeam: Panther's Stats\n--------------------\nTotal players: {len(team1["players"])}\nTotal experienced: {team1["experience"]}\nTotal inexperienced: {team1["inexperience"]}\nAverage height: {team1["avg_height"]}\nPlayers on Team: {players_on_teams(team1["players"])}\nGuardians: {guardians_on_teams(team1["players"])}"))
            input("\n To Continue Press Enter \n")
            menu_stats_tools()
        elif choice == "B"
            print(f"\nTeam: Bandits's Stats\n--------------------\nTotal players: {len(team1["players"])}\nTotal experienced: {team1["experience"]}\nTotal inexperienced: {team2["inexperience"]}\nAverage height: {team2["avg_height"]}\nPlayers on Team: {players_on_teams(team2["players"])}\nGuardians: {guardians_on_teams(team2["players"])}"))
            input("\n To Continue Press Enter \n")
            menu_stats_tools()
        elif choice == "C"
            print(f"\nTeam: Warriors' Stats\n--------------------\nTotal players: {len(team1["players"])}\nTotal experienced: {team1["experience"]}\nTotal inexperienced: {team3["inexperience"]}\nAverage height: {team3["avg_height"]}\nPlayers on Team: {players_on_teams(team3["players"])}\nGuardians: {guardians_on_teams(team3["players"])}"))
            input("\n To Continue Press Enter \n")
            menu_stats_tools()
        else:
            print("Invalid input. Please try again")
            menu_stats_tools()
    elif selection.upper == "B":
        exit()
    else:
        print("Error. Please try again")
        menu_stats_tool()
#Consolidate functions in one primary functions
def main():
    menu()
    clean_data()
    balance_teams()
    

if __name__ == "__main__":
    main()
    cleaned = clean_data(PLAYERS)
    balanced_teams = 