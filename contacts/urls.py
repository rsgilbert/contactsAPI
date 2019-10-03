from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('add/', views.add, name="add")
]