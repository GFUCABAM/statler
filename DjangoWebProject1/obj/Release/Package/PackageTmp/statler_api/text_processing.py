import requests

# Return a positivity rating for a review given the text of the review
def rateReview(text):
    rating = 0

    # make a POST request to the vivekn sentiment API, which returns the sentiment and the API's confidence in that
    # judgment.
    response = requests.post('http://sentiment.vivekn.com/api/text/', data={'txt' : text})
    json_result = response.json()['result']

    # if sentiment is positive, return confidence
    # if sentiment is negative, return -confidence
    # if sentiment is neutral, return 0
    if json_result['sentiment'] == 'Positive':
        rating = float(json_result['confidence'])
    elif json_result['sentiment'] == 'Negative':
        rating = -float(json_result['confidence'])

    return rating
