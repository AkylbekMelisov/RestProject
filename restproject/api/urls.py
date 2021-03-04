from django.urls import path
from .views import *



urlpatterns = [
    path('users/', UserView.as_view()),
    path('books/', BookView.as_view()),
    path('authors/', AuthorView.as_view())
]
