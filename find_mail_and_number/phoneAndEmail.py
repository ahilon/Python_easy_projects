#! python3
#phoneAndEmail.py - Wyszukuje numery telefonów i adresy email w schowku.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{2})?                    # Numer kierunkowy.
    (\s|-|\.)?                  # Separator.
    (\d{3})                     # Pierwsze trzy cyfry.
    (\s|-|\.)?                  # Separator.
    (\d{3})                     # środkowe 3 cyfry.
    (\s|-|\.)?                  # Separator.
    (\d{3})                     # ostatnie 3 cyfry.

    )''', re.VERBOSE)

# Utworzenie wyrażenia regularnego dopasowującego adres e-mail.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # nazwa użytkownika
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # nazwa domeny
    (\.[a-zA-Z]{2,4}){1,2}      # . i cokolwiek
    )''', re.VERBOSE)

# Wyszukanie dopasowań w schowku
text = str(pyperclip.paste())
phoneNumbers = []
emails = []

# Dopasowanie i formatowanie nr telefonu
for groups in phoneRegex.findall(text):
    phoneNum = groups[3] + '-' + groups[5] + '-' + groups[7]
    # Formatowanie nr telefonu z nr kierunkowym i wyświetlenie
    if groups[1]:
        phoneNumAreaCode = '+' + groups[1] + ' ' + phoneNum
        phoneNumbers.append(phoneNumAreaCode)
    # Formatowanie nr telefonu bez nr kierunkowego i wyświetlenie
    else:
        phoneNumbers.append(phoneNum)

#Wyświetlenie adresu email
for groups in emailRegex.findall(text):
    emails.append(groups[0])




if len(phoneNumbers) > 0:
    pyperclip.copy('\n'.join(phoneNumbers))
    print('Numery telefonów:')
    print('\n'.join(phoneNumbers))
    print("Znaleziono " + str(len(phoneNumbers)) + " numerów.")
else:
    print('Nie znaleziono żadnego numeru telefonu')

if len(emails) > 0:
    pyperclip.copy('\n'.join(emails))
    print('Adresy email:')
    print('\n'. join(emails))
    print("Znaleziono " + str(len(emails)) + " adresów email.")
else:
    print("Nie znaleziono żadnego adresu email")