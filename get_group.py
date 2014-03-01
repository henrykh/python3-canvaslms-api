import urllib.request
from canvaslms import api

# Load the oauth token
authToken = api.getAuthTokenFromFile("oauth.txt")

# Create the API object targeting the Evergreen Instructure instance
apiObj = api.CanvasAPI('evergreen.instructure.com', authToken)

values={
}
data = urllib.parse.urlencode(values)
binary_data = data.encode('ascii')
results = apiObj.allPages('courses/93/group_categories')
#results = apiObj.allPages('group_categories', args=binary_data)

#results = apiObj.allPages('conversations/:1754/add_message', args=binary_data)

print(len(results))

# Ordered dictionary
response_dict = results[0]

for (key,value) in response_dict.items():
	print(str(key) + ":" + str(value))
