'''
Here we search a string on twitter and add resultant tweets(& their sentiment analysis) to a CSV file
'''
import tweepy
import csv
from textblob import TextBlob

#Login to developer.twitter.com to get below details
consumer_key='**************************'
consumer_key_secret='**************************************************'

accessToken='**************************************************'
accessToken_secret='*********************************************'

auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
auth.set_access_token(accessToken,accessToken_secret)

TwitterApi =tweepy.API(auth)
tweets= TwitterApi.search(input('What do you want to search on twitter?\n'), count = 100)

#create a new CSV file & add column headings
with open('twitterResult.csv','w', encoding="utf-8") as resultFile:
	columns = ['Name', 'Twitter Handle', 'Tweet Text', 'Total Tweets', 'Favourites_Count', 'Followers', 'User_Id','User_Verified','User Location',
                 'Date of Tweet', 'Tweet Id', 'Language', 'Tweet Source', 'Tweet Retweet', 'Tweet Reply To Id',
                 'Reply To Name', 'SentimentAnalysis']
	writer= csv.DictWriter(resultFile, fieldnames= columns)
	writer.writeheader()

#Add Rows to the csv file
	for tweet in tweets:
		columnValues =([tweet.user.name, tweet.user.screen_name, tweet.text,
			tweet.user.statuses_count, tweet.user.favourites_count,	tweet.user.followers_count, 
			tweet.user.id, tweet.user.verified, tweet.user.location, tweet.user.created_at, tweet.id, 
			tweet.lang, tweet.source, tweet.retweet_count, tweet.in_reply_to_user_id, 
			tweet.in_reply_to_screen_name, str(TextBlob(tweet.text).sentiment)])
		#columnValues = [str(x).encode('utf-8') for x in columnValues]
		dictn = dict(zip(columns, columnValues))
		writer.writerow(dictn)
print('CSV file generated!')
