from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class EmployeeCreationView(TemplateView):
    template_name = 'employee_creation.html'