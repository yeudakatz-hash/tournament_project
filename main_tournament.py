from projects_week2.tournament.printer import print_menu, sort_menu
from projects_week2.tournament.validation import *
from projects_week2.tournament.manager import add_new_team, play, sorted_list
from projects_week2.tournament.arr_teams import teams


while True:
    choose = print_menu()
    if not check_choice(choose):
        print("error: try again\n")
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
        sort_by = sort_menu()
        li = sorted_list(sort_by)
        for l in li:
            print(l)


    elif choose == "5":
        pass


    elif choose == "6":
        pass


    elif choose == "7":
        pass


    elif choose == "8":
        pass


    elif choose == "9":
        pass


    elif choose == "10":
        pass

    elif choose == "0":
        break

    else:
        continue







#
# new_team = add_new_team()
# print("Team added successfully:", new_team)






