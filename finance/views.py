from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import JournalDefinition

# Create your views here.
class JournalDefinition(TemplateView):
    template_name = 'journal_definition.html'
    model = JournalDefinition