#! python3
import CreateZipFile as createZF
import sys
import os
import checkZipFile as checkZF


def getInfo():


    if whatToDo.lower() == 'a':
        fileName = input("Wybierz nazwę dla tworzonego pliku ZIP:\n")
        saveFilePathName = input("Podaj ścieżke do zapisu pliku:\n")
        filePath = input("Podaj ścieżke folderu do kompresji:\n")
        filePathName = input("Podaj nazwe pliku do konwersji:\n")


        CreateFilePath = createZF.CreateOrAddFileToZip(filePath, saveFilePathName, filePathName, fileName)
        CreateFilePath.addFileToZip()
        """
        checkZip = checkZF.CheckZip(filePath, filePathName)
        checkZip.checkZipFile()
        """



    elif whatToDo.lower() == 'c':
        fileName = input("Wybierz nazwę dla tworzonego pliku ZIP:\n")

        saveFilePathName = input("Podaj ścieżke do zapisu pliku:\n")

        filePath = input("Podaj ścieżke folderu do kompresji:\n")

        filePathName = input("Podaj nazwe pliku do konwersji:\n")

        CreateFilePath = createZF.CreateOrAddFileToZip(filePath, saveFilePathName, filePathName, fileName)
        CreateFilePath.createZip()

        checkZip = checkZF.CheckZip(saveFilePathName, fileName)
        checkZip.checkZipFile()



while True:
    whatToDo = input("Jeżeli chcesz stworzyć nowy plik wciśnij 'C', jeżeli chcesz dodać pliki wciśnij 'A'\n"
                     "jeżeli chcesz wyjśc z programu wciśnij losowy przycisk:\n")


    if whatToDo.lower() == 'a' or whatToDo.lower() == 'c':
        getInfo()
    else:
        print("Dziękuje za skorzystanie z programu")
        sys.exit()



