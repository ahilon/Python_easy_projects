import zipfile,os

class CreateOrAddFileToZip():

    def __init__(self, filePath,saveFilePath, filePathName, name):
        self.saveFilePath= saveFilePath
        self.folder = str(filePath) + "\\" + str(filePathName)
        self.name = name
        self.filePathName = filePathName


    def addFile(self,zipName, folder):
        for foldername, subfolders, filenames in os.walk(folder):
            print('Dodawanie plików w %s...' % (foldername))

            zipName.write(foldername)

            for filename in filenames:
                newBase = os.path.basename(folder) + '-'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue
                zipName.write(os.path.join(foldername, filename), compress_type=zipfile.ZIP_DEFLATED)
        zipName.close()
        print('gotowe!')

    def createZip(self):
        try:
            os.chdir(self.saveFilePath) # przechodzi do ścieżki, w której ma być zapisany plik
        except FileNotFoundError:
            os.mkdir(self.saveFilePath) # tworzy plik w podanej ścieżce jeżeli nie istnieje
            os.chdir(self.saveFilePath) # przechodzi do ścieżki, w której ma być zapisany plik

        folder = os.path.abspath(self.folder) #do zmiennej folder przypisuje ścieżkę bezwględną pliku


        zipFilename = self.name + '.zip' # przypisuje do zmiennej nazwe pliku z rozszerzeniem zip
        if os.path.exists(zipFilename): #jeżeli istnieje plik zip o podanej nazwie, tworzy nowy z koncówką "_liczba"
            number = 1
            while True:
                zipFilename = self.name + '_' + str(number) + '.zip'
                if not os.path.exists(zipFilename):
                    break
                number = number + 1

        print('tworzenie archiwum %s...' % (zipFilename))
        createZip = zipfile.ZipFile(zipFilename, 'w') #tworzy plik zip, i otwiera go w trybie zapisu

        self.addFile(createZip, folder) # wywołuje funkcje która dodaje pliki


    def addFileToZip(self):
        os.chdir(self.saveFilePath)
        folder = os.path.abspath(self.folder)

        zipFilename = self.name + '.zip'

        print('dodawanie pliku do archiwum %s...' % (zipFilename))
        addZip = zipfile.ZipFile(zipFilename, 'a')

        self.addFile(addZip, folder)

