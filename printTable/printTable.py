# Listy Zagnieżdzone
tableData = [
    ['jabłka', 'pomarańcze', 'wiśnie', 'banany'],
    ['Alicja', 'Bob', 'Karol', 'Dawid'],
    ['Psy', 'Koty', 'Łosie', 'Gęsi']
]
class CreateColumns():

    def __init__(self, tables):
        self.tables = tables
        # Utworzenie funkcji której zadaniem jest znalezienie najdłuższej zmiennej w liście

        # utworzenie listy, która składa się z 0, i jest tej długości co ilość podlist w liście głównej
        longestDataInEachList = [0] * len(self.tables)

        # Pętla której zadaniem jest znalezienie najdłuższej wartości każdej podlisty,
        # i zapisanie jej w liście longestDataInEachList
        iteration = 0
        for table in self.tables:
            longestData = 0
            for data in table:
                dataLen = len(data)
                if dataLen > longestData:
                    longestData = dataLen
                    longestDataInEachList[iteration] = dataLen
            iteration = iteration + 1

        # Znalezienie najdłuższej wartości w liście longestDataInEachList
        longestDataInEachList.sort()
        righwidth = longestDataInEachList[-1] + 1


        for table in self.tables:
            i = ""
            for item in table:
                i = i + item.rjust(righwidth)
            print(i)

CreateColumns(tableData)
