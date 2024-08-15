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
    
    if response.status_code == 404:
        print("Subreddit not found.")
        return
    elif response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print("No posts found.")
            return
        for post in posts:
            print(post.get('data', {}).get('title'))
    except ValueError:
        print("Error: Unable to parse JSON response")

if __name__ == "__main__":
    top_ten('python')
