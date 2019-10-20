import zipfile, os, sys

class CheckZip():

    def __init__(self,zipFileDir,zipName):
        self.zipFileDir = zipFileDir
        self.zipName = zipName
        self.fileSizes = {   # Słownik w którym zapisane zostaną wagi pliku przed i po kompresji
            "allFilesSize": 0,
            "allFilesCompressSize": 0,
        }



    def checkZipFile(self):

        try:
            os.chdir(self.zipFileDir) # Przejście do katalogu zawierającego plik .zip
            exampleZip = zipfile.ZipFile(self.zipName + '.zip') # Przypisanie do zmiennej pliku.zip
            zipFileList = exampleZip.namelist() #przypisanie do zmiennej, listy plików pliku.zip
            lenFiles = len(zipFileList) #sprawdzenie długości listy
        except FileNotFoundError:  # obsługa wyjątku, gdy ścieżka jest błedną lub nie ma w niej pliku, program sie kończy.
            print("Błędna ścieżka lub brak pliku o takiej nazwie w podanej ścieżce. Koniec programu.")
            sys.exit()

        for file in zipFileList:
            print("\nŚcieżka i nazwa pliku to: " + file)

            fileInfo = exampleZip.getinfo(file)  # przypisanie do zmiennej funkcji pobierającej informacje o pliku

            # przypisanie do zmiennej funkcji która pobiera informacje o wadze pliku przed kompresją
            fileSize = fileInfo.file_size # przypisanie do zmiennej informacji o wadze pliku przed kompresją
            print("Waga pliku przed kompresją " + str(fileSize) + " MB")

            # przypisanie do zmiennej funkcji która pobiera informacje o wadze pliku po kompresji
            compressSize = fileInfo.compress_size # przypisanie do zmiennej informacji o wadze pliku po kompresją
            print("Waga pliku po kompresji " + str(compressSize) + " MB")

            try:  # powstaje błąd gdy waga pliku jest mniejsza od 1
                print("skompresowany plik jest %sx mniejszy!" % (round(fileSize / compressSize, 2)))
            except ZeroDivisionError:
                print("waga pliku mniejsza niż 1 KB")

        # dodanie po kolei wagi każdego pliku przed i po kompresji, do odpowiedniego klucza w słowniku
            self.fileSizes["allFilesSize"] = self.fileSizes["allFilesSize"] + fileSize
            self.fileSizes["allFilesCompressSize"] = self.fileSizes["allFilesCompressSize"] + compressSize

            print("Plik zip " + "\"" + str(self.zipName) + "\"" + " zawiera w sobie pliki: " + str(zipFileList))
            print("Jest ich: " + str(lenFiles))

        allFilesSize = self.fileSizes["allFilesSize"]  # Przypisanie do zmiennej wagi wszystkich plików przed kompresją
        # Przypisanie do zmiennej wagi wszystkich plików po kompresji
        allFilesCompressSize = self.fileSizes["allFilesCompressSize"]

        # Wypisanie wagi wszystkich plików przed i po kompresji
        print("\nŁączna waga plików przed kompresją wynosi " + str(allFilesSize) + " MB.")
        print("Łączna waga plików po kompresji wynosi " + str(allFilesCompressSize) + " MB.")

        # Wypisanie wagi plików
        print("\nskompresowane pliki są %sx mniejsze od oryginału!" % (
            round((allFilesSize / allFilesCompressSize - 1), 2)))

        exampleZip.close() #zamknięcie pliku

