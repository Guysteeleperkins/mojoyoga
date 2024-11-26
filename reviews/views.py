from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Review
# Create your views here.

class ReviewList(generic.ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    paginate_by = 16

class LeaveReview(CreateView):
    model = Review
    fields = ['rating', 'content', 'image', 'is_anonymous']
    template_name = 'reviews/leave_a_review.html'
    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        is_anonymous = form.cleaned_data.get('is_anonymous')
        if is_anonymous:
            form.instance.author = None
        else:
            form.instance.author = self.request.user

        print(f"Form data - is_anonymous: {is_anonymous}, Author: {form.instance.author}")
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


# def review_edit(request, pk):
#     """
#     view to edit reviews
#     """
#     review = get_object_or_404(Review, pk=pk)

#     if request.method == "POST":
#         review_form = ReviewForm(request.POST, request.FILES, instance=review)
#         if review_form.is_valid():
#             review_form.save()
#             messages.success(request, "Review updated!")
#             return redirect('reviews')
#         else:
#             messages.error(request, "Error updating review!")
#     else:
#         review_form = ReviewForm(instance=review)

#     return render(request, 'reviews/leave_a_review.html', {'review_form': review_form, 'review':review,})


