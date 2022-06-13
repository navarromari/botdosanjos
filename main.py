import gspread
from twitter import *

# Authentication process
all_keys = open('twitterkeys', 'r').read().splitlines()

consumer_key = all_keys[0]
consumer_secret = all_keys[1]
token = all_keys[2]
token_secret = all_keys[3]

gc = gspread.service_account('credentials.json')
t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# Open a sheet from a spreadsheet in one go
wks = gc.open("augusto-dos-anjos-bot").sheet1

#set next tweet as the first cell of "tweets" column
next_tweet = wks.acell('A2').value

#add the current tweet to the end of the "tweets" column (creating a loop)
wks.append_row([next_tweet])

#post tweet through twitter API
t.statuses.update(status=next_tweet)

#delete the row we just tweeted
wks.delete_rows(2)