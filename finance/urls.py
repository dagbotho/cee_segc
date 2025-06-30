from django.urls import path

from .views import JournalDefinition


urlpatterns = [
    path('journal-definition/', JournalDefinition.as_view()),
]