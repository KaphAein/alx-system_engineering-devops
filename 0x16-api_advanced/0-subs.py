import requests

def number_of_subscribers(subreddit):
    '''queries the Reddit API and returns the number of subscribers'''

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'subreddit-subscriber-counter/0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

