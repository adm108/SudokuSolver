from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Sudoku(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    solve_counter = models.PositiveIntegerField(null=True)

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

    # Fields for solved sudoku
    case00s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case01s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case02s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case03s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case04s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case05s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case06s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case07s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case08s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case10s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case11s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case12s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case13s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case14s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case15s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case16s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case17s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case18s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case20s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case21s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case22s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case23s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case24s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case25s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case26s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case27s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case28s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case30s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case31s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case32s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case33s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case34s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case35s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case36s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case37s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case38s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case40s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case41s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case42s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case43s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case44s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case45s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case46s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case47s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case48s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case50s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case51s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case52s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case53s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case54s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case55s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case56s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case57s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case58s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case60s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case61s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case62s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case63s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case64s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case65s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case66s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case67s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case68s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case70s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case71s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case72s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case73s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case74s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case75s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case76s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case77s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case78s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    case80s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case81s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case82s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case83s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case84s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case85s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case86s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case87s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    case88s = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    class Meta:
        verbose_name_plural = "Sudoku"
