import requests

# Return a positivity rating for a review given the text of the review
def rateReview(text):
    rating = 0

    # make a POST request to the vivekn sentiment API, which returns the sentiment and the API's confidence in that
    # judgment.
    response = requests.post('http://sentiment.vivekn.com/api/text', data={'txt' : text})
    response.json()

    # if sentiment is positive, return confidence
    # if sentiment is negative, return -confidence
    # if sentiment is neutral, return 0
    if response['sentiment'] == 'Positive':
        rating = response['confidence']
    elif response['sentiment'] == 'Negative':
        rating = -response['confidence']

    return rating
