from . import views
from django.urls import path

urlpatterns = [
    path('', 
        views.WelcomePage.as_view(), name='home'),
]
