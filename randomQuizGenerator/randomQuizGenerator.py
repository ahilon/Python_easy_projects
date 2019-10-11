#! python3
# randomQuizGenerator.py - tworzy losowy quiz, z pytaniami i odpowiedziami.
import random as rn

# to są dane quizu. klucz to nazwa stanu, a wartość to stolica.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
capitalsItems = list(capitals.items())

#Wygenerowanie 5 plików quizu.
for quizNum in range(5):
    #utworzenie plików quizu i odpowiedzi na pytania
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum +1 ), 'w')

    # zapis nagłówka quizu.
    quizFile.write('Imie i nazwisko:\n\nData:\n\nKlasa:\n\n')
    quizFile.write((' ' * 20) + 'Quiz stolica stanów (Quiz %s)' % (quizNum +1))
    quizFile.write('\n\n')

    # losowe ustalenie kolejności stanów
    states = list(capitals.keys())
    rn.shuffle(states)

    # iteracja przez 50 stanów i utworzenie pytania dotyczącego każdego z nich
    for questionNum in range(50):
        # Przygotowanie prawidłowych i nieprawidłowych odpowiedzi.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = rn.sample(wrongAnswers, 3)

        answerOptions = wrongAnswers + [correctAnswer]
        rn.shuffle(answerOptions)

        # Zapis pytania i odpowiedzi w pliku quizu.
        quizFile.write('%s. Co jest stolicą stanu %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('     %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Zapis odpowiedzi w pliku.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()