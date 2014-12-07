import sys
import json



def main():
    tweet_file = open(sys.argv[1])
    scores = {}

    total = 0
    count = 0
   		 
    for line in tweet_file:
    	data = json.loads(line)
	for key, value in data.iteritems() :
    		if key == "text":
    			for word in value.split() :
    				word = word.lower() 
    				found = 0
    				for term, score in scores.iteritems():
    					if (term == word):
    						found = 1;
				if (found == 1):
					count = count +1
					#print word,scores[word], "found\n", 
					scores[word] = scores[word]  + 1
					#print scores[word]
				else:
					#print word, "new\n"
					scores[word] =  1
				total = total + 1

    #print count, total		
    for term, score in scores.iteritems():	
		print term+"\t"+str(float(scores[term])/float(total))
	
if __name__ == '__main__':
    main()
