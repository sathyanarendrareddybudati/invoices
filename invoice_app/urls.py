from django.urls import path
from .views import InvoicesAPI

urlpatterns = [
    path('invoices/', InvoicesAPI.as_view()),
    path('invoices/<int:pk>/', InvoicesAPI.as_view()),
]