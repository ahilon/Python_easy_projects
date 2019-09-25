class Restaurant():
    """fdfd"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.customer_per_week = 0
        self.customer_all_time = 0

    def describe_restaurant(self):
        print("Nasza restauracja nazywa się: " + self.restaurant_name)
        print("Profil działania restauracji to kuchnia: " + self.cuisine_type)

    def open_restaurant(self):
        print("Godziny otwarcia:\nPoniedziałek - Piątek 8.00 - 21.00\nSobota 8.00-23.00\nNiedziela 9.00-22.00\n")

    def increment_customer(self, day_of_the_week, day_customers):
        self.day_of_the_week = day_of_the_week
        self.day_customers = day_customers


        print("Dziś jest " + self.day_of_the_week + " i restauracje " + self.restaurant_name + " odwiedziło " +
        self.day_customers + " klientów.")


        if self.day_of_the_week == "niedziela":
            self.customer_all_time += int(self.day_customers)
            self.customer_per_week += int(self.day_customers)
            print("W tym tygodniu odwiedziło nas " + str(self.customer_per_week) + " klientów.")
            self.customer_per_week = 0

        else:
            self.customer_all_time += int(self.day_customers)
            self.customer_per_week += int(self.day_customers)
            print("Od początku tygodnia do " + self.day_of_the_week + " restauracje odwiedziło " +
                  str(self.customer_per_week) + " klientów." )

    def all_visit(self):
        print("Dotychczas odwiedziło nas " + str(self.customer_all_time) + " klientów")



restaurant_1 = Restaurant("taj life", "tajlandzka")

print("Nazwa restauracji to: " + restaurant_1.restaurant_name.title() + ".")
print("Profil działania to kuchnia: " + restaurant_1.cuisine_type.title() + ".")


def end_of_the_day(end_of_day_customer, restaurant_number):
    name_of_the_day = input("Jaki jest dzień tygodnia:\nDla poniedziałek wybierz '1'\nDla wtorek wybierz '2'"
                            "\nDla środa wybierz '3\nDla czwartek wybierz '4'\nDla piątek wybierz '5'"
                            "\nDla sobota wybierz '6'\nDla niedziela wybierz'7'\n")
    print(name_of_the_day)
    day = ""
    if int(name_of_the_day) == 1:
         day = "poniedziałek"

    elif int(name_of_the_day) == 2:
        day = "wtorek"
    elif int(name_of_the_day) == 3:
        day = "środa"

    elif int(name_of_the_day) == 4:
        day = "czwartek"

    elif int(name_of_the_day) == 5:
        day = "piątek"

    elif int(name_of_the_day) == 6:
        day = "sobota"

    elif int(name_of_the_day) == 7:
        day = "niedziela"

    else:
        print( "coś poszło nie tak")
        end_of_day_customer == 0

    return restaurant_number.increment_customer(day, str(end_of_day_customer))

restaurant_1 = Restaurant("taj life", "tajlandzka")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

while True:
    today_visitors = input("Podaj liczbę klientów którzy odwiedzili lokal:\n")
    end_of_the_day(int(today_visitors), restaurant_1)

    end_loop = input("jeżeli chcesz zakończyć program, wpisz 'koniec', "
                     "jeśli chcesz kontynuować naciśnik dowolny klawisz\n")

    if end_loop == "koniec":
        break


restaurant_1.all_visit()