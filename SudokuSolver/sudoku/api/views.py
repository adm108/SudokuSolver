from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from sudoku.api.permissions import IsAuthorOrReadOnly
from sudoku.api.serializers import SudokuBeforeSolveSerializer, SolvedSudokuSerializer
from sudoku.models import SudokuBeforeSolve


class SudokuBeforeSolveViewSet(viewsets.ModelViewSet):
    queryset = SudokuBeforeSolve.objects.all()
    lookup_field = "slug"
    serializer_class = SudokuBeforeSolveSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
