from django.contrib import admin
from sudoku.models import SudokuBeforeSolve, SolvedSudoku

admin.site.register(SudokuBeforeSolve)
admin.site.register(SolvedSudoku)
