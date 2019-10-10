import json

filename = "username.json"

def greet_user():
    ###przywitanie użytkownika
    username = get_storaged_name()
    while True:
        true_name = input("Czy " + username + " to poprawna nazwa? jeżeli tak wciśnij 't':\n")
        if true_name.lower() == "t":
            print("Witaj ponownie " + username + " cieszę się z twojego powrotu")
            break

        else:
            username = add_new_name()


#Utworzenie nowego pliku i zapisanie nazwy
def add_new_name():
    username = input("Podaj swoje imie:\n")
    filename = "username.json"
    with open(filename, "w") as file_with_name:
        json.dump(username, file_with_name)
        return username

# Funkcja która pobiera zapisane imię z pliku username.json
def get_storaged_name():
    filename = "username.json"
    try:
        with open(filename) as file_with_name:
            username = json.load(file_with_name)
            print(username)
            return username
        #Gdy w folderze nie ma pliku o nazwie "username.json" program przechodzi do funkcji która tworzy nowy plik
    except FileNotFoundError:
        new_name = add_new_name()
        return new_name


greet_user()