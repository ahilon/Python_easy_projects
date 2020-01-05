#! Python 3
# stopwatch.py

import time

#Wyświetlanie informacji o sposobie działania programu.
print('Naciśnij Enter, aby rozpocząć pomiar. Każde kolejne naciśnięcie klawisza Enter, oznacza nowe okrążenie')
print('Naciśięcie Ctrl + C kończy działanie programu')
input()
print('Rozpoczęto pomiar.')
startTime = time.time()
lastTime = startTime
lapNum = 1

#Rozpoczęcie pomiaru czasu okrążenia.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Okrążenie #%s: %s sec (%s)' % (lapNum, totalTime, lapNum), end='')
        lapNum += 1
        lastTime = time.time()

except KeyboardInterrupt:
    #Obsługa wyjątku zgłaszanego po naciśnięciu klawiszy CTRL + C.
    print('\nGotowe!')
