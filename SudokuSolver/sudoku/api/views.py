from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from sudoku.api.permissions import IsAuthorOrReadOnly
from sudoku.api.serializers import SudokuSerializer
from sudoku.models import Sudoku
from sudoku.api import sudoku_algorithm
import time


class SudokuViewSet(viewsets.ModelViewSet):
    queryset = Sudoku.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = SudokuSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # to view only request.user's records
        author_queryset = []
        for element in queryset:
            if element.author == self.request.user:
                author_queryset.append(element)

        page = self.paginate_queryset(author_queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(author_queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        board = []
        line = []
        for i in range(0, 9):
            for j in range(0, 9):
                if self.request.data[f"case{i}{j}"] == None:
                    line.append(0)
                else:
                    line.append(self.request.data[f"case{i}{j}"])
            board.append(line)
            line = []

        # solving sudoku algorithm with time of running
        start = time.time()
        results = sudoku_algorithm.solve(board)
        end = time.time()
        algorithm_time = end - start

        serializer.save(
            author=self.request.user,
            solve_counter=results[1],
            solve_time=algorithm_time,
            case00s=results[0][0][0],
            case01s=results[0][0][1],
            case02s=results[0][0][2],
            case03s=results[0][0][3],
            case04s=results[0][0][4],
            case05s=results[0][0][5],
            case06s=results[0][0][6],
            case07s=results[0][0][7],
            case08s=results[0][0][8],
            case10s=results[0][1][0],
            case11s=results[0][1][1],
            case12s=results[0][1][2],
            case13s=results[0][1][3],
            case14s=results[0][1][4],
            case15s=results[0][1][5],
            case16s=results[0][1][6],
            case17s=results[0][1][7],
            case18s=results[0][1][8],
            case20s=results[0][2][0],
            case21s=results[0][2][1],
            case22s=results[0][2][2],
            case23s=results[0][2][3],
            case24s=results[0][2][4],
            case25s=results[0][2][5],
            case26s=results[0][2][6],
            case27s=results[0][2][7],
            case28s=results[0][2][8],
            case30s=results[0][3][0],
            case31s=results[0][3][1],
            case32s=results[0][3][2],
            case33s=results[0][3][3],
            case34s=results[0][3][4],
            case35s=results[0][3][5],
            case36s=results[0][3][6],
            case37s=results[0][3][7],
            case38s=results[0][3][8],
            case40s=results[0][4][0],
            case41s=results[0][4][1],
            case42s=results[0][4][2],
            case43s=results[0][4][3],
            case44s=results[0][4][4],
            case45s=results[0][4][5],
            case46s=results[0][4][6],
            case47s=results[0][4][7],
            case48s=results[0][4][8],
            case50s=results[0][5][0],
            case51s=results[0][5][1],
            case52s=results[0][5][2],
            case53s=results[0][5][3],
            case54s=results[0][5][4],
            case55s=results[0][5][5],
            case56s=results[0][5][6],
            case57s=results[0][5][7],
            case58s=results[0][5][8],
            case60s=results[0][6][0],
            case61s=results[0][6][1],
            case62s=results[0][6][2],
            case63s=results[0][6][3],
            case64s=results[0][6][4],
            case65s=results[0][6][5],
            case66s=results[0][6][6],
            case67s=results[0][6][7],
            case68s=results[0][6][8],
            case70s=results[0][7][0],
            case71s=results[0][7][1],
            case72s=results[0][7][2],
            case73s=results[0][7][3],
            case74s=results[0][7][4],
            case75s=results[0][7][5],
            case76s=results[0][7][6],
            case77s=results[0][7][7],
            case78s=results[0][7][8],
            case80s=results[0][8][0],
            case81s=results[0][8][1],
            case82s=results[0][8][2],
            case83s=results[0][8][3],
            case84s=results[0][8][4],
            case85s=results[0][8][5],
            case86s=results[0][8][6],
            case87s=results[0][8][7],
            case88s=results[0][8][8],
        )

