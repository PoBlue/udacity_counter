# -*- coding:utf-8 -*-
"""
froum counter
"""
from time import sleep
from datetime import date, timedelta
from selenium import webdriver
from bs4 import BeautifulSoup
import froum_database


class FroumRequest():
    """
    get the data from udacity forum
    """
    def __init__(self, forum_url, web_driver_path):
        self.forum_url = forum_url
        self.post_id = "ember1020"
        self.theme_id = "ember1019"
        self.web_driver_path = web_driver_path

    def get_html(self):
        """
        get forum html text
        """
        driver = webdriver.Chrome(self.web_driver_path)
        driver.get(self.forum_url)
        sleep(3)
        return driver.page_source

    def get_number_with_id(self, element_id):
        """
        get the data in froum page with id
        """
        html_text = self.get_html()
        soup = BeautifulSoup(html_text, "lxml")
        count = soup.find(id=element_id).find("span", {"class": "number"}).string
        return int(count)

    def get_all_count(self):
        """
        get the sum of theme and post data in froum page
        """
        html_text = self.get_html()
        soup = BeautifulSoup(html_text, "lxml")
        count_of_post = soup.find(id=self.post_id).find("span", {"class": "number"}).string
        count_of_theme = soup.find(id=self.theme_id).find("span", {"class": "number"}).string
        count = int(count_of_post) + int(count_of_theme)
        return count

    def get_post_count(self):
        """
        get the count of post
        """
        return self.get_number_with_id(self.post_id)

    def get_theme_count(self):
        """
        get the count of theme
        """
        return self.get_number_with_id(self.theme_id)


class FroumCounter(FroumRequest):
    """
    class that handler froum counter
    """
    def __init__(self, forum_url, web_driver_path):
        FroumRequest.__init__(self, forum_url, web_driver_path)
        self.money_each_forum = 20
        self.base_day = 12

    def get_money_day(self, _days):
        """
        get money from days ago
        """
        _yesterday_date = date.today() - timedelta(days=_days + 1)
        forum_data = froum_database.get_forum_data_recently(_yesterday_date)
        new_count = self.get_all_count()
        self.add_count_date(new_count, date.today())
        return (new_count - forum_data.count) * self.money_each_forum

    def get_money_month(self):
        """
        return money that a this month
        """
        _month_ago_date = date.today() - timedelta(days=30)
        _base_date = date(date.today().year, date.today().month, self.base_day)
        if date.today() < _base_date:
            _base_date = date(_month_ago_date.year, _month_ago_date.month, self.base_day)
        forum_data = froum_database.get_forum_data_recently(_base_date)
        new_count = self.get_all_count()
        self.add_count_date(new_count, date.today())
        return (new_count - forum_data.count) * self.money_each_forum

    def add_count_day(self, count, year, month, day):
        """
        add a new data to database
        """
        new_date = date(year, month, day)
        self.add_count_date(count, new_date)

    def add_count_date(self, count, _date):
        """
        add a new data to database
        """
        forum_data = froum_database.get_forum_in_date(_date)
        if forum_data is not None:
            froum_database.update_forum_count(_date, count)
        else:
            froum_database.add_forum_data(count, _date)
