import base64
import gspread
import tweepy

def post_tweet(event, context):

    # Authentication process
    all_keys = open('twitterkeys', 'r').read().splitlines()

    consumer_key = all_keys[0]
    consumer_secret = all_keys[1]
    token = all_keys[2]
    token_secret = all_keys[3]
    bearer_token = all_keys[4]  

    client = tweepy.client(bearer_token, consumer_key, consumer_secret, token, token_secret)
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, token, token_secret)
    api = tweepy.API(auth)

    gc = gspread.service_account('credentials.json')

    # Open a sheet from a spreadsheet in one go
    wks = gc.open("augusto-dos-anjos-bot").sheet1

    #set next tweet as the first cell of "tweets" column
    next_tweet = wks.acell('A2').value

    #add the current tweet to the end of the "tweets" column (creating a loop)
    wks.append_row([next_tweet])

    #post tweet through twitter API
    client.create_tweet(text = next_tweet)

    #delete the row we just tweeted
    wks.delete_rows(2)