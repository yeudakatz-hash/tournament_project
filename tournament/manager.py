from .validation import *





#מקבל id ןמעביר הלאה לבדיקה
def get_id(action):
    id_team = input("Enter ID team: ")
    if action == "add":
        while is_id_exists(id_team) or not check_id(id_team):
            while is_id_exists(id_team):
                print("this id is taken, enter another id: ")
                id_team = input("Enter ID team")
            while not check_id(id_team):
                print("Invalid ID. Must be a positive number.")
                id_team = input("Enter id team: ")


    elif action == "check":
        while not is_id_exists(id_team) or not check_id(id_team):
            while not is_id_exists(id_team):
                print("This ID not found: ")
                id_team = input("Enter ID team")
            while check_id(id_team):
                print("Invalid ID. Must be a positive number.")
                id_team = input("Enter id team: ")

    return str_to_int(id_team)



#מקבל שם ןמעביר הלאה לבדיקה
def get_name():
    name_team = input("Enter name team: ")
    while check_name(name_team):
        print("Invalid name. Cannot be empty.")
        name_team = input("Enter name team: ")
    return name_team.strip()


def play():
    team1 = get_id("check")
    team2 = get_id("check")
    while team1 == team2:
        print("same ID. enter different IDs: ")
        team1 = get_id("check")
        team2 = get_id("check")
    goals_team1 = input("Enter num of goals of team1: ")
    while not check_goals(goals_team1):
        print("Illegal goals")
        goals_team1 = input("Enter num of goals of team1: ")
    goals_team2 = input("Enter num of goals of team2: ")
    while not check_goals(goals_team2):
        print("Illegal goals")
        goals_team2 = input("Enter num of goals of team2: ")
    update_goals(team1, team2 , goals_team1, goals_team2)

    return teams







def add_new_team():
    team = {
        "id" : get_id("add"),
        "name" : get_name(),
        "played" : 0,
        "wins": 0,
        "draws" : 0,
        "goals for" : 0,
        "goals against" : 0,
        "points" : 0
    }
    return team


def sorted_list(num):
    table = None
    num = str_to_int(num)
    if num == 1:
        table = sorted(teams, key= lambda t: t["points"], reverse=True)
    elif num == 2:
        table = sorted(teams, key= lambda t: t["goals"], reverse=True)
    elif num == 3:
        table = sorted(teams, key= lambda t: t["goals for"] - t["goals against"], reverse=True)
    elif num == 4:
        table = sorted(teams, key= lambda t: t["name"])
    return table



def calculate_success():
    success_rate = None
    name = input("enter group name: ")
    while not is_name_exists(name):
        print("try again")
        name = input("enter group name: ")
    for team in teams:
        if team["name"] == name:
            success_rate = 100 * (int(team["points"]) / (3 * int(team["played"])))
    return success_rate