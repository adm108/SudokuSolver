from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class SudokuBeforeSolve(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    case00 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case01 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case02 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case03 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case04 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case05 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case06 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case07 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case08 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case10 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case11 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case12 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case13 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case14 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case15 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case16 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case17 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case18 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case20 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case21 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case22 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case23 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case24 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case25 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case26 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case27 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case28 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case30 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case31 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case32 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case33 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case34 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case35 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case36 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case37 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case38 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case40 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case41 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case42 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case43 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case44 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case45 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case46 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case47 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case48 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case50 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case51 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case52 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case53 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case54 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case55 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case56 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case57 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case58 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case60 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case61 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case62 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case63 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case64 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case65 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case66 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case67 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case68 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case70 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case71 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case72 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case73 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case74 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case75 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case76 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case77 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case78 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case80 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case81 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case82 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case83 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case84 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case85 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case86 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case87 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case88 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    class Meta:
        verbose_name_plural = "Sudoku before solve"


class SolvedSudoku(models.Model):
    sudoku_before_solve = models.OneToOneField(
        SudokuBeforeSolve, on_delete=models.CASCADE, default=None
    )

    case00 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case01 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case02 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case03 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case04 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case05 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case06 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case07 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case08 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case10 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case11 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case12 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case13 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case14 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case15 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case16 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case17 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case18 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case20 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case21 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case22 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case23 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case24 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case25 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case26 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case27 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case28 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case30 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case31 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case32 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case33 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case34 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case35 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case36 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case37 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case38 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case40 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case41 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case42 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case43 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case44 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case45 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case46 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case47 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case48 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case50 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case51 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case52 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case53 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case54 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case55 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case56 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case57 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case58 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case60 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case61 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case62 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case63 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case64 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case65 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case66 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case67 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case68 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case70 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case71 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case72 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case73 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case74 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case75 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case76 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case77 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case78 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case80 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case81 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case82 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case83 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case84 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case85 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case86 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case87 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case88 = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    class Meta:
        verbose_name_plural = "Solved sudoku"
