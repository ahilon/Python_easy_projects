import CreateZipFile as CZF
import sys
import os

while True:
    filePath = input("Podaj ścieżke folderu do kompresji:\n")
    filePathName = input("Podaj nazwe pliku do konwersji:\n")

    filename = input("Wybierz nazwę dla tworzonego pliku ZIP:\n")

    CreateFilePath = CZF.CreateOrAddFileToZip(filePath, filePathName, filename)

    whatToDo = input("Jeżeli chcesz stworzyć nowy plik wciśnij 'w', jeżeli chcesz dodać pliki wciśnij 'a':\n")

    if whatToDo.lower() == 'a':
        CreateFilePath.addFileToZip()
        sys.exit()
    elif whatToDo.lower() == 'w':
        CreateFilePath.CreateZip()
        sys.exit()
    else:
        print("błąd")

