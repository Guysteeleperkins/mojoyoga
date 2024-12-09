from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class WelcomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'welcome/index.html'

class AboutPage(TemplateView):
    """
    Displays about page"
    """
    template_name = 'welcome/about.html'