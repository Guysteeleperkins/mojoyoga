from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='reviews'),
    path('<int:pk>', views.review_detail, name='review_detail'),
]

