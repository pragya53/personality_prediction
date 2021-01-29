import tweepy as tw

consumer_key='ANXCHb996ZyO6LMOAh9Uq9EMi'
consumer_secret ='EiUGos8M9xRPJnawN9QpdsWGVEY3j7PmwAE7EnAQaDg7m8WYIJ'
access_token='1348652957051408385-XRei0L07XAR4XkmHvhjOGKMsCAAPRp'
access_token_secret ='OIOx1itlZaJ0cT41S4pw4g1Wj7IkjyiMYXtPdpjD88XXz'

def fetch(handle):
	# Authenticate
	auth = tw.OAuthHandler(consumer_key, consumer_secret)
	# Set Tokens
	auth.set_access_token(access_token, access_token_secret)
	# Instantiate API
	api = tw.API(auth, wait_on_rate_limit=True)

	res = api.user_timeline(screen_name=handle, count=100, include_rts=True)
	tweets = [tweet.text for tweet in res]
	text = ''.join(str(tweet) for tweet in tweets)
	return text

