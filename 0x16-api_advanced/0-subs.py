#!/usr/bin/python3
""" api advanced """

import requests


def number_of_subscribers(subreddit):
    """
    api advan """
    base_url = "https://www.reddit.com/r/"

    url = "{}{}/about.json".format(base_url, subreddit)
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 \
                    Safari/537.36 Edg/123.0.0.0"
    }
    results = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if results.status_code == 200:
        return results.json()["data"]["subscribers"]
    return 0
