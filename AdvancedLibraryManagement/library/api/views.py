from library.models import Author, Book, Loan
from .serializers import AuthorSerializer, BookSerializer, LoanSerializer
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class AuthorVS(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class BookVS(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class LoanVS(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer