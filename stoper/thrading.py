import time, datetime, threading

firstTime = datetime.timedelta(minutes=2)

secondTime = datetime.timedelta(minutes=1)

thirdTime = datetime.timedelta(seconds=30)

print('Uruchomienie programu...')

def firstThread():
    time.sleep(10)
    print("Pierwsze zadanie")

def secondThread():
    time.sleep(8)
    print("Drugie zadanie")

def thirdThread():
    time.sleep(5)
    print("Trzecie zadanie")

threadFirst = threading.Thread(target=firstThread)
threadSecond = threading.Thread(target=secondThread)
threadThird = threading.Thread(target=thirdThread)

firstThread()
secondThread()
thirdThread()

threadFirst.start()
threadSecond.start()
threadThird.start()