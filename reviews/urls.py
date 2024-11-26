from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewList.as_view(), name='reviews'),
    path('<int:pk>', views.review_detail, name='review_detail'),
    path('leave-a-review/', views.LeaveReview.as_view(), name='leave_review'),
]
