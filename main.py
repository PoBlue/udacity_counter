# -*- coding:utf-8 -*-
"""
main center
"""
from review_counter import ReviewCounter
from froum_counter import FroumRequest

StartFroumCount = 534
Token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozMTQ0MywiZXhwIjoxNDk3NzM3NDcwLCJ0b2tlbl90eXBlIjoiYXBpIn0.lkJmwgDSZzz-Arhn5JTRX5P6Wi1cAmbGP9DMlOL8YRQ'
Url = 'http://discussions.youdaxue.com/users/_Mo/summary'
review_counter = ReviewCounter(Token)
forum_counter = FroumRequest(Url)
# print(review_counter.get_count_today(0))
# print(review_counter.get_count_month(0))
print(review_counter.get_money_month(0))
# print(forum_counter.get_post_count())
# print(forum_counter.get_theme_count())
print(forum_counter.get_all_count() - StartFroumCount)