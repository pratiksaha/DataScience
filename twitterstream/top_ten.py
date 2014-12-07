import sys
import json



def main():
    tweet_file = open(sys.argv[1])
    hashtexts = {}		 
    for line in tweet_file:
    	data = json.loads(line)
	for key, value in data.iteritems() :
    		if key == "entities":
    			hashtags = value["hashtags"]
    			#print hashtags, type(hashtags)
    			for hashtext in hashtags:
    				word = hashtext["text"]
    				#print word
    				#print hashtext["text"]
    				found = 0
    				for term, score in hashtexts.iteritems():
    					if (term == word):
    						found = 1;
				if (found == 1):
					#count = count +1
					#print word,scores[word], "found\n", 
					hashtexts[word] = hashtexts[word]  + 1
					#print scores[word]
				else:
					#print word, "new\n"
					hashtexts[word] =  1
					#total = total + 1
    
    for  i in range(0,10):
    	maxcount = 0
    	maxhash = ""
    	for hashtext, count in hashtexts.iteritems() :	
    		if count > maxcount:
    			maxcount = count
    			maxhash = hashtext
	print maxhash, maxcount
	if maxhash in hashtexts:
		del hashtexts[maxhash]
		
if __name__ == '__main__':
    main()
