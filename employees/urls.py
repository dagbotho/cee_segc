from django.urls import path

from .views import EmployeeCreationView

urlpatterns = [
    path('employee-creation/', EmployeeCreationView.as_view()),
]