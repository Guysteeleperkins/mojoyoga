from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review
# Create your views here.

class ReviewList(generic.ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    paginate_by = 8

def review_detail(request, pk):
    """
    Display an individual :model:`review.Review`.

    **Context**

    ``review``
        An instance of :model:`review.Review`.

    **Template:**

    :template:`reviews/review_detail.html`
    """
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'reviews/review_detail.html', {'review': review})
