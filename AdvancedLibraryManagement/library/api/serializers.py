from rest_framework import serializers
from library.models import Author, Book, Loan

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)
    class Meta:
        model = Author
        fields = "__all__"
        
class BookSerializer(serializers.ModelSerializer):
    loans = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = "__all__"
        
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"