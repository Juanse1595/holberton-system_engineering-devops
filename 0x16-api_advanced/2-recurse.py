#!/usr/bin/python3
'''2-recurse module'''
import requests


def recurse(subreddit, hot_list=[], idx=0):
    headers = {
        'User-Agent': 'Example script to retrieve info'
    }
    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit), headers=headers)
    if response.reason != 'OK':
        return None
    else:
        if idx == len(response.json()['data']['children']):
            return hot_list
        hot_list.append(response.json()['data']['children']
                        [idx]['data']['title'])
        return recurse(subreddit, hot_list, idx + 1)
