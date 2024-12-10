from . import views
from django.urls import path

urlpatterns = [
    path('', views.WelcomePage.as_view(), name='welcome'),
    path('about', views.AboutPage.as_view(), name='about'),
    path('gallery', views.GalleryPage.as_view(), name='gallery'),
]
