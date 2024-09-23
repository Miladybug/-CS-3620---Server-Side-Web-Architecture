from django.urls import path, include
from .api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('author', views.AuthorVS, basename="author")
router.register('book', views.BookVS, basename="book")
router.register('loan', views.LoanVS, basename="loan")

urlpatterns = [
    path('', include(router.urls)),
]
