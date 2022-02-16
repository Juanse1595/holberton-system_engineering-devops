#!/usr/bin/python3
'''1-top_ten module'''
import requests


def top_ten(subreddit):
    headers = {
        'User-Agent': 'Example script to retrieve info'
    }
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit), headers=headers)
    if response.reason != 'OK':
        print('None')
    else:
        for item in response.json()['data']['children']:
            print("{}".format(item['data']['title']))
