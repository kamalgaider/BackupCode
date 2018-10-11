from textblob import TextBlob
#print sentiment associated with words (output is between -1 & 1)
s= TextBlob("angry sad hate love happy shocked devastating excited salvation")
print(s.words)
print(s.tags)
print(s.sentiment.polarity)