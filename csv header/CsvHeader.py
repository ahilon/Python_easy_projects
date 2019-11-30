#! python3
# removeCsvHeader.py -- Usuwanie nagłówka we wszystkich plików CSV.
# znajdujących sie w bieżącym katalogu roboczym.

import csv, os

os.chdir("examples")
os.makedirs('headerRemoved', exist_ok=True)

# Iteracja przez wszystkie pliki w bieżacym katalogu roboczym.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Usuwanie nagłówka z pliku ' + csvFilename + '...')

    #odczyt plików CSB z pominieciem pierwszego wiersza
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # Pominięcie pierwszego wiersza.
        csvRows.append(row)
    csvFileObj.close()

    #TODO: zapis pliku csv.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()