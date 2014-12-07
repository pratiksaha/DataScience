import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=coursera")
pyresponse =  json.load(response)
#print type(pyresponse)
#results = pyresponse["query"]
#for key, value in pyresponse.iteritems() :
   # 		print key #, value
print len(results)
for i in range(len(results)):
	print results[i]["text"]

print pyresponse["query"]
