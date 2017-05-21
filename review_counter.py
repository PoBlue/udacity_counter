# !/usr/bin/python
# -*- coding:utf-8 -*-
'''
review counter
'''
import requests
from time import gmtime, strftime
from datetime import datetime, timedelta


class ReviewRequest():
    """
    Class that request review data
    """
    def __init__(self, token):
        self.token = token
        self.cetification_url = 'https://review-api.udacity.com/api/v1/me/certifications.json'
        self.comleted_url = 'https://review-api.udacity.com/api/v1/me/submissions/completed'

    def get_certifications(self):
        """
        get certifications of review
        """
        return self.get_method(self.cetification_url).json()

    def get_method(self, url, params=None):
        """
        review get method
        """
        headers = {'Authorization': self.token, 'Content-Length': '0'}
        response = requests.get(url, headers=headers, params=params)
        return response

    def get_review_completed_in_time(self, start_time):
        """
        get review completed when it is from start_time
        """
        params = {'start_date': start_time}
        response = self.get_method(self.comleted_url, params=params)
        return response.json()


class ReviewCounter(ReviewRequest):
    """
    handle the count of review
    """
    def __init__(self, token):
        ReviewRequest.__init__(self, token)

    def get_count_today(self):
        """
        get count of reviews in today
        """
        return len(self.get_reviews_today())

    def get_reviews_today(self):
        """
        get review that is completed today
        """
        time_format = "%Y-%m-%dT00:00:00Z"
        yesterday = datetime.now() - timedelta(days=1)
        start_time = yesterday.strftime(time_format)
        return self.get_review_completed_in_time(start_time)


Token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozMTQ0MywiZXhwIjoxNDk3NzM3NDcwLCJ0b2tlbl90eXBlIjoiYXBpIn0.lkJmwgDSZzz-Arhn5JTRX5P6Wi1cAmbGP9DMlOL8YRQ'
review_counter = ReviewCounter(Token)
print(review_counter.get_count_today())