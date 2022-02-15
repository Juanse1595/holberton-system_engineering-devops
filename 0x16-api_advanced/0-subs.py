#!/usr/bin/python3
'''0-subs module'''
import requests
import sys


def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'Example script to retrieve info'
    }
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit), headers=headers)
    if response.reason != 'OK':
        return 0
    return response.json()['data']['subscribers']
