from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('budget/', views.BudgetAPiView.as_view(), name = 'budgets')
]

