from django.urls import path

from .views import SignupPageView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    # Add other URLs for the accounts app here
]