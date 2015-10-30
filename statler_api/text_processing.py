from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

# Return a positivity rating for a review given the text of the review
def rateReview(text):
    rating = 0
    return rating