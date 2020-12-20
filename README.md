# SudokuSolver 

## DESCRIPTION
Czy wiesz co to jest backtracking algorithm? Jeśli nie to dobrze trafiłeś :). Stworzyłem prostą aplikację webową, która umożliwia rozwiązanie tablicy sudoku przy pomocy właśnie tego algorytmu. W skrócie: backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution [wikipedia].
Innym ciekawym zastosowaniem tego algorytmu jest tzw. eight queens puzzle problem, który polega na tym żeby umiejscowić na szachownicy 8 chess queens tak aby, żadna z nich nie mogła zbić jednym ruchem innej [wikipedia]
W kontekście mojej aplikacji backtracking szuka pustego pola w tablicy sudoku, nadaje mu numer 1 i sprawdza czy tablica jest poprawna. Jeżeli nie, to nadaje mu kolejny numer (2) i sprawdza po raz kolejny aż do 9 numeru. Jeżeli algorytm znajdzie poprawny numer to przechodzi do kolejnego pustego pola, jeśli nie to cofa się o jedno pole i szuka kolejnego numeru dla poprzedniego pola. Brzmi trochę skomplikowanie, ale jest to stosunkowo prosty algorytm. Jego wadą jest bardzo duża ilość wywołań funkcji w przypadku bardzo trudnych sudoku. W aplikacji jest możliwość podejrzenia ilości wywołań funkcji dla każdego rozwiązania oraz czasu trwania algorytmu.

Aplikację stworzyłem ponieważ chciałem przećwiczyć frontendowy framework Vue.js w połączeniu z API w DRF oraz chciałem poprawić swoje skille w HTML i CSS a także JS. ;)

## FEATURES
- Tworzenie konta (rejestracja) oraz logowanie do aplikacji
- Sprawdzenie poprawności wprowadzonych liczb do tablicy
- Rozwiązanie sudoku poprzez backtracking algorithm
- Podejrzenie rozwiązanych tablic sudoku wraz ze statysytkami działania algorytmu (czas działania oraz liczba wywołań funkcji)
- Usuwanie rozwiązanych sudoku

## TECHNOLOGIES AND LIBRARIES
Main technologies:
- Python 3.9.1
- Django 3.0.8
- Django Rest Framework 3.11.1
- Vue.js 2.6.11
- HTML 5
- CSS 3
- JavaScript
- Bootstrap

Libraries for connecting frontend with backend:
- django webpack_loader 0.7.0
- webpack bundle tracker

Libraries for creating registration and login forms:
- django-crispy-forms 1.9.2

Libraries for user authentication:
- django-allauth 0.42.0
- django-registration 3.1
- django-rest-auth 0.9.5

Future features:
- creating accounts,
- solving sudoku puzzle,
- archive with solved sudoku with its algorithm's time and number of function call


- each sudoku has:
    - an owner
    - created_at field
    - algorithm time
    - number of function call
    - sudoku with empty places -> before solving

from django.contrib.auth import get_user_model
custom_user = get_user_model()
u = custom_user.objects.first()
from sudoku.models import SudokuBeforeSolve
s = SudokuBeforeSolve.objects.create(author=u, a1b1=5)

admin-may7ap

- webpack bundle trucker and django webpack loader for communicate backend and frontend with eachother