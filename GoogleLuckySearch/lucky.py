#! python3
# lucky.py

import requests, sys, webbrowser, bs4

print('Wyszukiwanie...')    #Komunikat wyświetlany podczas pobierania strony Google.
res = requests.get('http://google.pl/search?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()

#Pobranie łaczy z kilkoma pierwszymi wynikami wyszukiwania
soup = bs4.BeautifulSoup(res.text, "html.parser")

#Otworzenie karty przeglądarki WWW dla każdego wyniku wyszukiwania.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.pl' + linkElems[i].get('href'))