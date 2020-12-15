# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:14:25 2019

@author: CLCG200532
"""

intervals = (
    ('m', 2540160),  # 60 * 60 * 24 * 7 * 4.2 aprox
    ('w', 604800),  # 60 * 60 * 24 * 7
    ('d', 86400),    # 60 * 60 * 24
    ('h', 3600),    # 60 * 60
    ('m', 60),
    ('s', 1),
    )

def display_time(seconds, granularity=6):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            result.append("{}{}".format(value, name))
    return ' '.join(result[:granularity])