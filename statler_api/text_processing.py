from django.http import HttpRequest
import json

# Return a positivity rating for a review given the text of the review
def rateReview(text):
    rating = 0

    # make a POST request to the vivekn sentiment API, which returns the sentiment and the API's confidence in that
    # judgment.
    json_data = HttpRequest.POST("http://sentiment.vivekn.com/api/text", data=text)
    parsed_data = json.loads(json_data)

    # if sentiment is positive, return confidence
    # if sentiment is negative, return -confidence
    # if sentiment is neutral, return 0
    if parsed_data["sentiment"] == "Positive":
        rating = parsed_data["confidence"]
    elif parsed_data["sentiment"] == "Negative":
        rating = -parsed_data["confidence"]

    return rating
