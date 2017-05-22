# -*- coding:utf-8 -*-
'''
review counter
'''
from datetime import datetime, timedelta
import requests


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
        return len(self.get_reviews_before_days(0))

    def get_reviews_before_days(self, days):
        """
        get review that is completed from days
        """
        time_format = "%Y-%m-%dT00:00:00Z"
        start_date = datetime.now() - timedelta(days=days+1)
        start_time = start_date.strftime(time_format)
        return self.get_review_completed_in_time(start_time)

    def get_reviews_before_months(self, monthes):
        """
        get review that is comleted in this month
        """
        time_format = "%Y-%m-01T00:00:00Z"
        start_date = datetime.now() - timedelta(days=monthes*30)
        start_time = start_date.strftime(time_format)
        return self.get_review_completed_in_time(start_time)

    def get_count_month(self):
        """
        get the count of reviews in this month
        """
        return len(self.get_reviews_before_months(0))

    def get_money_today(self, before_days):
        """
        get the sum of the money in reviews that is completed today
        """
        sum_money = 0
        today_reviews = self.get_reviews_before_days(before_days)
        for review in today_reviews:
            sum_money += float(review['price'])
        return sum_money

    def get_money_month(self, before_months):
        """
        get money in this month
        """
        sum_money = 0
        month_reviews = self.get_reviews_before_months(before_months)
        for review in month_reviews:
            sum_money += float(review['price'])
        return sum_money
