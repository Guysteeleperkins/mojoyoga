from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from allauth.account.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
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


class GalleryPage(TemplateView):
    """
    Displays about page"
    """
    template_name = 'welcome/gallery.html'