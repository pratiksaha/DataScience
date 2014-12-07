import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print len(str(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    sent_file = open(sys.argv[2])
    scores = {}
    for line in tweet_file:
    		score  = line.split("\t")
		scores[score[0]] = int(score[1]) 		 
    for line in sent_file:
    	data = json.loads(line)
	for key, value in data.iteritems() :
    		if key == "text":
    			sent = 0
    			for word in value.split(" ") : 
    				for term, score in scores.iteritems():
    					if term == word:
    						sent = sent + score

    			print sent			

    	


	
if __name__ == '__main__':
    main()
