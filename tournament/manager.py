from  projects_week2.tournament.validation import *
from projects_week2.tournament.arr_teams import teams



#צריך בדיקה שלא יהיה 2 קבוצות עם אותו שם וid



#מקבל id ןמעביר הלאה לבדיקה
def get_id(action):
    id_team = input("Enter ID team: ")
    while check_id(id_team):
        print("Invalid ID. Must be a positive number.")
        id_team = input("Enter id team: ")
        if action == "add":
            while not is_id_exists(id_team):
                print("this id is taken, enter another id: ")
                id_team = input("Enter ID team")
        if action == "check":
            while is_id_exists(id_team):
                print("This ID not found: ")
                id_team = input("Enter ID team")
    return int(id_team)



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


    # return team1 , team2 , goals_team1 , goals_team2




def add_new_team():
    team = {
        "id" : get_id("add"),
        "name" : get_name(),
        "played" : 0,
        "wins": 0,
        "draws" : 0,
        "goals for" : 0,
        "goals_against" : 0,
        "points" : 0
    }
    return team


def add_new_play():
    team1 = get_id("check")
    team2 = get_id("check")
    while team1 == team2:
        print("enter again id ")
        team1 = get_id()
        team2 = get_id()
    return team1, team2



