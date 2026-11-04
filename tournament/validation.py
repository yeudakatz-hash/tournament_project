from projects_week2.tournament.arr_teams import teams

#המרה הstr לint
def str_to_int(string):
    try:
        return int(string)
    except ValueError:
        return None

def is_id_exists(team_id):
    return any(team["id"] == str_to_int(team_id) for team in teams)

def is_name_exists(team_name):
    return any(team["name"].strip().lower() == team_name.strip().lower() for team in teams)


#בדיקת חוקיות id
def check_id(id_team):
    val = str_to_int(id_team)
    return isinstance(val, int) and val > 0


#בדיקת חוקיות שם
def check_name(name_team):
    if not isinstance(name_team, str):
        return False
    clean_name = name_team.strip()
    return len(clean_name) > 0 and not clean_name.isdigit() and is_name_exists(clean_name)


def check_goals(num):
    num = str_to_int(num)
    return isinstance(num , int) and num >= 0


#בדיקת חוקיות פעולה
def check_choice(choice):
    val = str_to_int(choice)
    return val is not None and 0 <= val <= 10


def update_goals(id_team1, id_team2 , goals_team1 , goals_team2):
    for team in teams:
        if team["id"] == id_team1:
            team["goals for"] = goals_team1
            team["goals against"] = goals_team2
            team["played"] += 1
            if goals_team1 > goals_team2:
                team["wins"] += 1
                team["points"] += 3
            elif goals_team1 == goals_team2:
                team["draws"] += 1
                team["points"] += 1


        if team["id"] == id_team2:
            team["goals for"] = goals_team2
            team["goals against"] = goals_team1
            team["played"] += 1
            if goals_team2 > goals_team1:
                team["wins"] += 1
                team["points"] += 3
            elif goals_team1 == goals_team2:
                team["draws"] += 1
                team["points"] += 1

    return teams













