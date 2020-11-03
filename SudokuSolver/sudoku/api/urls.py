from django.urls import include, path
from rest_framework.routers import DefaultRouter
from sudoku.api import views as qv

router = DefaultRouter()
router.register(r"sudoku", qv.SudokuViewSet)

urlpatterns = [path("", include(router.urls))]
