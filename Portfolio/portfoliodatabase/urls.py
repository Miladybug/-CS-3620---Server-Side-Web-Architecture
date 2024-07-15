from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="Home"),
    path('hobbies/', views.hobbies, name="Hobbies"),
    path('portfolio/', views.portfolio, name="Portfolio"),
    path('contact/', views.contact, name="Contact")
    
]