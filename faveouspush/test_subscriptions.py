import imp
fb = imp.load_source('fb', 'fbconsole.py')

"""
First we need to obtain access token for application management:
https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials"
"""

"""
http://developers.facebook.com/docs/reference/api/user/
User object supports Real-Time Updates for the following connections: feed, friends, activities, interests, music, books, movies, television, likes, checkins.
"""

APP_ID = '243799762330010'

fb.authenticate()
print fb.graph('/%s' % fb.APP_ID)
print fb.graph('/%s/subscriptions' % fb.APP_ID)

print fb.graph_post('/%s/subscriptions' % fb.APP_ID, {
	'object': 'user',
	'fields': 'feed,likes',
	'callback_url': 'http://188.165.17.198/test.php',
	'verify_token': 'aaa'
	})

# http://localhost:8000/
# http://188.165.17.198/test.php	