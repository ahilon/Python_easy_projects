import zipfile,os

class CreateOrAddFileToZip():

    def __init__(self, filePath,saveFilePath, filePathName, name = ""):
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
        test = os.chdir(self.saveFilePath) # przechodzi do ścieżki, w której ma być zapisany plik
        print(test)
        folder = os.path.abspath(self.folder) #do zmiennej folder przypisuje ścieżkę bezwględną pliku
        print(folder)

        zipFilename = self.name + '.zip'
        if os.path.exists(zipFilename):
            number = 1
            while True:
                zipFilename = self.name + '_' + str(number) + '.zip'
                if not os.path.exists(zipFilename):
                    break
                number = number + 1

        print('tworzenie archiwum %s...' % (zipFilename))
        createZip = zipfile.ZipFile(zipFilename, 'w')

        self.addFile(createZip, folder)


    def addFileToZip(self):

        folder = os.path.abspath(self.folder)

        zipFilename = self.name + '.zip'

        print('dodawanie pliku do archiwum %s...' % (zipFilename))
        addZip = zipfile.ZipFile(zipFilename, 'a')
        self.addFile(addZip, folder)

