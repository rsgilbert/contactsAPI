from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('add/', views.add, name="add"),
    path('contacts/', views.ContactList.as_view()),
    path('finance/', views.FinanceList.as_view()),
]