from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Review
from .forms import ReviewForm
# Create your views here.

class ReviewList(generic.ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    paginate_by = 16

    def get_queryset(self):
        return Review.objects.all().order_by('-created_on') 

class LeaveReview(CreateView):
    model = Review
    fields = ['rating', 'content', 'image',]
    template_name = 'reviews/leave_a_review.html'
    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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


def review_edit(request, pk):
    """
    view to edit review
    """
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated!")
            return redirect('reviews')
        else:
            messages.error(request, "Error updating review!")
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/review_edit.html', {'form': form, 'review':review,})

def review_delete(request, pk):
    """
    view to delete review
    """
    review = get_object_or_404(Review, pk=pk)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return redirect('reviews')


