#!/usr/bin/python3
'''2-recurse module'''
import requests


def recurse(subreddit, hot_list=[]):
    headers = {
        'User-Agent': 'Example script to retrieve info'
    }
    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit), headers=headers)
    if response.reason != 'OK':
        return None
    else:
        for item in response.json()['data']['children']:
            hot_list.append(item['data']['title'])
        return hot_list
