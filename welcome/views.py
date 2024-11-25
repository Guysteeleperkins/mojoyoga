from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class WelcomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'
