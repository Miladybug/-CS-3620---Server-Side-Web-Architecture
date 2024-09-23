from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.last_name + ", " + self.first_name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publication_date = models.DateField()
    
    def __str__(self):
        return self.title
    
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    borrower  = models.CharField(max_length=100)
    loan_date = models.DateField()
    return_date = models.DateField()
    
    def __str__(self):
        return self.borrower + ", " + str(self.return_date)