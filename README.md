# SudokuSolver 

## DESCRIPTION
Do you know what backtracking algorithm is? If not, you have come to the right place :). I created a simple web application that allows you to solve a sudoku table using this algorithm. In short: backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution [[wikipedia]](https://en.wikipedia.org/wiki/Backtracking).
Another interesting using of this algorithm is so-called the eight queens puzzle problem. The problem is to place 8 chess queens on the board so that none of them can capture another with one move [[wikipedia]](https://en.wikipedia.org/wiki/Eight_queens_puzzle). In the context of my application, backtracking looks for an empty field in the sudoku board, put on that place number 1 and checks if the all board is correct. If not, it put on the same place number 2 and checks again up to number 9. If the algorithm finds the correct number it goes to the next empty field, if not it goes back one field and looks for that field the next number. It sounds a little complicated, but it is a relatively simple algorithm. Its disadvantage is the large number of functions calls in the case of very difficult sudoku. The application allows to view the number of function calls for each solution and the duration of the algorithm.

I created this application because I wanted to practice Vue.js frontend framework in conjunction with Django Rest Framework and I wantend to improve my skils in HTML, CSS and JS ;).

## FEATURES
- Creating an account (registration) and login into the application
- Validation the numbers entered into the sudoku board
- Solving sudoku via backtracking algorithm
- Algorithm operation statistics (operation time and number of backtracking function calls)
- Removing solved sudoku

## TECHNOLOGIES AND LIBRARIES
Main technologies:
- Python 3.9.1
- JavaScript
- Django 3.0.8
- Django Rest Framework 3.11.1
- Vue.js 2.6.11
- HTML 5
- CSS 3
- Bootstrap 4.5.0

Libraries for connecting frontend with backend:
- django webpack_loader 0.7.0
- webpack bundle tracker 0.4.3

Libraries for creating registration and login forms:
- django-crispy-forms 1.9.2

Libraries for user authentication:
- django-allauth 0.42.0
- django-registration 3.1
- django-rest-auth 0.9.5

## HOW TO INSTALL LOCALY?
1. Create folder for app.
2. Open your code editor inside that folder.
3. Create virtual environment and activate it:
```sh
$ python -m venv venv (if you work on Windows system)
```
4. Clone repository:
```sh
$ git clone https://github.com/adm108/SudokuSolver.git
```
5. Go to SudokuSolver folder where requirements.txt file is and install all packages:
```sh
$ pip install -r requirements.txt
```
6. Use manage.py to enter following commands. Generate SQL commands:
```sh
$ python manage.py makemigrations
```
7. Execute SQL commands:
```sh
$ python manage.py migrate
```
8. Create superuser (enter email, username and password):
```sh
$ python manage.py createsuperuser
```
9. Go to frontend folder and install all frontend packages (you should have node.js engine installed on your system):
```sh
$ npm install
```
10. Now you can open 2 terminal windows and run 2 local servers (frontend and backed). Inside frontend folder:
```sh
$ npm run serve
```
11. Inside SudokuSolver folder (where manage.py is):
```sh
$ python manage.py runserver
```
12. You can log in using superuser account or you can create the new one and then you can use backtracking algorithm to solve your sudoku!

## LICENCE
It is a open source project. Anybody is free to use, study, modify and distribute this project for any purpose.

## RESOURCES
##### Great course about Django, Django REST Framework and Vue.js frameworks. It shows how to use all above mentioned technologies in one project [[Michele Saba]](https://www.udemy.com/course/the-complete-guide-to-django-rest-framework-and-vue-js/)

##### Simple explanation how to write backtracking algorithm for solving sudoku board [[Tech With Tim]](https://www.youtube.com/playlist?list=PLzMcBGfZo4-kE3aF6Y0wNBNih7hWRAU2o)

##### Cool concept for creating sudoku board in HTML and CSS also with checking the correctness of the entered values [[Morgan Schmiedt]](https://www.youtube.com/watch?v=O-rR1iuzhmU&t=1257s&ab_channel=MorganSchmiedt)

## SOME SCREENS FROM THE APP
<div align="center">Registration form</div>

![alt text](screens/registration.jpg)
***
<div align="center">Login form</div>

![alt text](screens/login.jpg)
***
<div align="center">Sudoku board with CLEAR, VERIFY and SOLVE buttons. Shot screen after clicking VERIFY button</div>

![alt text](screens/board.jpg)
***
<div align="center">Solved sudoku with statistics</div>

![alt text](screens/solved.jpg)
***
<div align="center">List of solved sudoku with DELETE and LOAD MORE buttons</div>

![alt text](screens/list.jpg)
