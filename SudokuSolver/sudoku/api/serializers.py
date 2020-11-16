from rest_framework import serializers
from sudoku.models import Sudoku


class SudokuSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    # sudoku_count = serializers.SerializerMethodField()

    class Meta:
        model = Sudoku
        fields = "__all__"

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d-%m-%Y %H:%M:%S")

    # def get_sudoku_count(self, instance):
    #     return instance.
