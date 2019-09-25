import random

game = "1"
best_result = 0

welcome = " Cześć! Masz szanse zagrać w niesamowitą gre kosmici!\nGra jest bardzo prosta.\n"
instruction_1 = " Kosmici są bardzo przebiegli, w każdej rundzie dwóch z nich to tylko hologramy, musisz zgadnąć który"
instruction_1 += " jest prawdziwy.\nWybierz kolor kosmity, i przekonaj się czy masz racje.\n"
alien_green = " \nJeżeli wybierzesz kosmitę zielonego i trafisz możesz dostać 5 punktów i 1 szanse,"
alien_green += " \njeżeli nie trafisz tracisz 1 szanse."
alien_red = " \nJeżeli wybierzesz kosmitę czerwonego i trafisz możesz dostać 10 punktów i 2 szanse, "
alien_red += " \njeżeli nie trafisz tracisz 2 szanse."
alien_yellow = " \nJeżeli wybierzesz kosmitę żółtego i trafisz  możesz dostać 15 punktów i 3 szanse, "
alien_yellow += " \njeżeli nie trafisz tracisz 3 szanse.\n"
instruction_2 = " \nJeżeli wybierzesz inną liczbę niż '1' czyli zielony. '2' czyli czerwony lub '3' czyli zółty"
instruction_2 += " Tracisz kolejkę.\n Powodzenia!"

print(welcome + instruction_1 + alien_green + alien_red + alien_yellow + instruction_2)

while game == "1":

    point = 0
    chances = 5

    while chances > 0:
        number_of_color = random.randrange(1, 4)

        choice = input (" \nwybierz kolor kosmity do zestrzelenia : wpisz '1' dla koloru zielonego,"
                        "\n'2' dla koloru czerwonego + lub '3' dla koloru żółtego: \n ")
        print(" Twój wybór to " + choice)

        if choice == "1":

            if number_of_color == 1 and int(choice) == 1:
                print(" Brawo zestrzeliłeś zielonego kosmitę dostajesz 5 punktów")
                point += 5
            else:
                print(" Pudło! poprawny nr kosmity to " + str(number_of_color))
                chances -= 1

        elif  choice == "2":
            if number_of_color == 2 and int(choice) == 2:
                print(" Brawo zestrzeliłeś czerwonego kosmitę dostajesz 10 punktów")
                point += 10
                chances += 1
            else:
                chances -= 2
                print(" Pudło! poprawny nr kosmity to " + str(number_of_color))

        elif choice == "3":
            if number_of_color == 3 and int(choice) == 3:
                print(" Brawo zestrzeliłeś żółtego kosmitę dostajesz 15 punktów")
                point += 15
                chances += 2
            else:
                chances -= 3
                print(" Pudło! poprawny nr kosmity to " + str(number_of_color))

        else:
            print(" Chyba wybrałeś złą liczbe, tracisz kolejkę")
            chances -= 1


    if point > 0:
        print(" Zdobyłeś " + str(point) + " punktów. Gratulacje!")
    else:
        print(" Nie udało ci się zdobyć żadnego punktu. przegrałeś")

    last_game = int(point)

    if last_game > best_result:
        print (" Twój nowy rekord to " + str(last_game) + " Brawo!")
        best_result = last_game

    game = input(" jeżeli chcesz zagrać ponownie wciśnij '1', w przeciwnim wypadku wciśnij dowolny klawisz:\n")
    if game == "1":
        chances = 5

print (" Twój najlepszy wynik to " + str(best_result) + " Brawo!")