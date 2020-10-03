from django.apps import AppConfig


class SudokuConfig(AppConfig):
    name = 'sudoku'

    def ready(self):
        import sudoku.signals
