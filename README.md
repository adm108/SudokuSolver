"# SudokuSolver" 

Page under construction.
Django Rest Framework + Vue.js
- django rest-auth
- django allauth
- django-registration
- django crispy-form

- django webpack_loader
- webpack bundle tracker

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