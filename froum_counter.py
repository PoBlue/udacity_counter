# -*- coding:utf-8 -*-
"""
froum counter
"""
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup


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

    def get_money_day(self, days):
        """
        get money from days ago
        """
        return self.get_all_count() * self.money_each_forum