from tournament.printer import print_menu, sort_menu
from tournament.manager import *
import logging





logging.basicConfig(
    filename="tournament.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)






while True:
    choose = print_menu()
    if not check_choice(choose):
        print("error: try again\n")
        logging.warning(f"Invalid menu choice: {choose}")
        continue

    if choose == "1":
        teams.append(add_new_team())

    elif choose == "2":
        if len(teams) > 0:
            for team in teams:
                print(team)
        else:
            print("The list of teams is empty. ")

    elif choose == "3":
        play()


    elif choose == "4":
        pass


    elif choose == "5":
        sort_by = sort_menu()
        li = sorted_list(sort_by)
        for l in li:
            print(l)


    elif choose == "6":
        for team in teams:
            if team["played"] > 0:
                print(sorted_list(1)[0])
            else:
                print("No games yet")


    elif choose == "7":
        first_place = sorted_list(1)
        print(first_place[0])
        all_teams = sorted_list(1)
        for team in all_teams(range(1 , len(all_teams))):
            if team["goals"] == first_place["goals"]:
                print(team["name"])



    elif choose == "8":
        for team in teams:
            if team["played"] > 0:
                success = calculate_success()
                print(success, "%")
        print("no games yet.")


    elif choose == "9":
        for team in teams:
            if int(team["played"]) > 0 and int(team["wins"]) == 0:
                print(team["name"] , team["played"] , team["points"])



    elif choose == "10":
        pass

    elif choose == "0":
        break

    else:
        continue







#
# new_team = add_new_team()
# print("Team added successfully:", new_team)






