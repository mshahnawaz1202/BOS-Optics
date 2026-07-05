from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('book/', views.book_appointment, name='book'),
]
