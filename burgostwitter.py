import tweepy
import time


def parse_tweet_url(tweet_json):
    try:
        url = tweet_json['entities']['urls'][0]['expanded_url']
        cleaned_url = url.split('?')[0]
    except IndexError:
        cleaned_url = 'https://www.twitter.com'
    return cleaned_url


class TwitterBot:

    'Simple class to Interact with the Twitter API'

    def __init__(self, access_token, access_token_secret,
                 consumer_key, consumer_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self._api = tweepy.API(auth)

    def search(self, link, since_id=None):
        search_link = link.split('://')[1]
        response = tweepy.Cursor(
            self._api.search,
            q=search_link,
            rpp=100,
            since_id=since_id,
        )

        # TODO: collect tweepy.error.TweepError error
        for page in response.pages():
            for status in page:
                    yield self.read_status(status, link)
            time.sleep(6)

    def read_status(self, status, search_url):
        # A better way to process Tweepy individual results
        nt = status._json
        new_twitter_user = dict(
            description=nt['user']['description'],
            followers_count=nt['user']['followers_count'],
            friends_count=nt['user']['friends_count'],
            id_str=nt['user']['id_str'],
            location=nt['user']['location'],
            name=nt['user']['name'],
            screen_name=nt['user']['screen_name'],
            verified=nt['user']['verified'],
        )
        new_tweet = dict(
            id_str=nt['id_str'],
            favorite_count=nt['favorite_count'],
            text=nt['text'],
            retweeted=nt['retweeted'],
            retweet_count=nt['retweet_count'],
            link_url=parse_tweet_url(nt),
            fake_news_url=search_url,
            user=new_twitter_user
        )
        return new_tweet
