#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        print(post.get('data', {}).get('title'))


if __name__ == "__main__":
    top_ten('python')
