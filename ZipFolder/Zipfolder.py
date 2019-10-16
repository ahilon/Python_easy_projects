
import zipfile, os, sys

"""Pobranie od użytkownika ścieżki do pliku, w którym znajduje się plik .zip i Pobranie od użytkownika nazwy pliku .zip
 bez rozszerzenia """

zipFileDir = input("Podaj ścieżke w której znajduje się plik: \n")
zipName = input("Podaj nazwe pliku zip, bez rozszerzenia: \n")


try:
    os.chdir(zipFileDir)  # Przejście do katalogu zawierającego plik .zip
    exampleZip = zipfile.ZipFile(zipName + '.zip') # Przypisanie do zmiennej pliku.zip
    zipFileList = exampleZip.namelist() #przypisanie do zmiennej, listy plików pliku.zip
    lenFiles = len(zipFileList)
except FileNotFoundError: #obsługa wyjątku, gdy ścieżka jest błedną lub nie ma w niej pliku, program sie kończy.
    print("Błędna ścieżka lub brak pliku o takiej nazwie w podanej ścieżce. Koniec programu.")
    sys.exit()

#Utworzenie słownika, w którym zapisane będą wagi wszystkich plików przed i po kompresji


fileSizes = {
        "allFilesSize" : 0,
        "allFilesCompressSize" : 0,
    }

def checkZipFileList(fileList):
    """ funkcja interuje wszystki pliki wewnatrz pliku .zip, następnie pokazuje wage pliku przed i po kompresji, i jaka
    jest róznica w wagach.
    :param fileList: zmienna w której znajduje się lista z plikami wewnątrz pliku .zip
    """
    for file in fileList:
        print("\nŚcieżka i nazwa pliku to: " + file)
        fileInfo = exampleZip.getinfo(file) #przypisanie do zmiennej funkcji pobierającej informacje o pliku

        # przypisanie do zmiennej funkcji która pobiera informacje o wadze pliku przed kompresją
        fileSize = fileInfo.file_size
        print("Waga pliku przed kompresją " + str(fileSize) + " MB")

        # przypisanie do zmiennej funkcji która pobiera informacje o wadze pliku po kompresji
        compressSize = fileInfo.compress_size
        print("Waga pliku po kompresji " + str(compressSize) + " MB")

        try: #powstaje błąd gdy waga pliku jest mniejsza od 1
            print("skompresowany plik jest %sx mniejszy!" % (round(fileSize / compressSize, 2)))
        except ZeroDivisionError:
            print("waga pliku mniejsza niż 1 KB")

        #dodanie po kolei wagi każdego pliku przed i po kompresji, do odpowiedniego klucza w słowniku
        fileSizes["allFilesSize"] = fileSizes["allFilesSize"] + fileSize
        fileSizes["allFilesCompressSize"] = fileSizes["allFilesCompressSize"] + compressSize

def checkZipFile():
    """Funkcja ma zadanie wypisanie ilości plików w ZIPie, następnie wypisanie wagi plików przed i po kompresji,
    i sprawdza o ile mniejsza jest waga plików po kompresji"""
    print("Plik zip " + "\"" + str(zipName) + "\"" + " zawiera w sobie pliki: " + str(zipFileList))
    print("Jest ich: " + str(lenFiles))

    allFilesSize = fileSizes["allFilesSize"]  # Przypisanie do zmiennej wagi wszystkich plików przed kompresją
    # Przypisanie do zmiennej wagi wszystkich plików po kompresji
    allFilesCompressSize = fileSizes["allFilesCompressSize"]

    # Wypisanie wagi wszystkich plików przed i po kompresji
    print("\nŁączna waga plików przed kompresją wynosi " + str(allFilesSize) + " MB.")
    print("Łączna waga plików po kompresji wynosi " + str(allFilesCompressSize) + " MB.")

    # Wypisanie wagi plików
    print("\nskompresowane pliki są %sx mniejsze od oryginału!" % (round((allFilesSize / allFilesCompressSize - 1), 2)))


# Funkcja if sprawdza czy w pliku zip, jest przynajmniej jeden plik, dopiero wtedy wykonuje się program
if lenFiles > 0:
    checkZipFileList(zipFileList)  # Wywołanie funcji
    checkZipFile()

else:
    print("Ten plik ZIP jest pusty!")

#zamknięcie pliku
exampleZip.close()


