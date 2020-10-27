from rest_framework import serializers
from sudoku.models import SudokuBeforeSolve, SolvedSudoku


class SudokuBeforeSolveSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = SudokuBeforeSolve
        fields = "__all__"

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d-%m-%Y %H:%M:%S")


class SolvedSudokuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolvedSudoku
