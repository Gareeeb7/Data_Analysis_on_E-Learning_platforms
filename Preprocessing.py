import tweepy
import re
import pandas as pd

df = pd.read_csv("onlinelearning.csv")
tweets = df.values.tolist()

     
# Preprocessing the tweets
for list in tweets:
   for tweet in list:
       tweet = re.sub(r'^https://t.co/[a-zA-Z0-9]*\s', " ", tweet)
       tweet = re.sub(r'\s+https://t.co/[a-zA-Z0-9]*\s', " ", tweet)
       tweet = re.sub(r'\s+https://t.co/[a-zA-Z0-9]*$', " ", tweet)
       tweet = tweet.lower()
       tweet = re.sub(r"that's","that is",tweet)
       tweet = re.sub(r"there's","there is",tweet)
       tweet = re.sub(r"what's","what is",tweet)
       tweet = re.sub(r"where's","where is",tweet)
       tweet = re.sub(r"it's","it is",tweet)
       tweet = re.sub(r"who's","who is",tweet)
       tweet = re.sub(r"i'm","i am",tweet)
       tweet = re.sub(r"she's","she is",tweet)
       tweet = re.sub(r"he's","he is",tweet)
       tweet = re.sub(r"they're","they are",tweet)
       tweet = re.sub(r"who're","who are",tweet)
       tweet = re.sub(r"ain't","am not",tweet)
       tweet = re.sub(r"wouldn't","would not",tweet)
       tweet = re.sub(r"shouldn't","should not",tweet)
       tweet = re.sub(r"can't","can not",tweet)
       tweet = re.sub(r"couldn't","could not",tweet)
       tweet = re.sub(r"won't","will not",tweet)
       tweet = re.sub(r"\W"," ",tweet)
       tweet = re.sub(r"\d"," ",tweet)
       tweet = re.sub(r"\s+[a-z]\s+"," ",tweet)
       tweet = re.sub(r"\s+[a-z]$"," ",tweet)
       tweet = re.sub(r"^[a-z]\s+"," ",tweet)
       tweet = re.sub(r"\s+"," ",tweet)
   print(tweets) 
