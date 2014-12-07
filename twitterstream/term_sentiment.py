import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}    
    for line in sent_file:
    		term, score  = line.split("\t")
		scores[term] = int(score)
 
    tweets = {} 
    words = {}		 
    for line in tweet_file:
    	data = json.loads(line)
	for key, value in data.iteritems() :
    		if key == "text":
    			#print value
    			sent = 0
    			for word in value.split() : 
    				#print word
    				foundinaffin = 0
    				for term, score in scores.iteritems():
    					if term == word:
						sent = sent + score
						foundinaffin = 1
				if foundinaffin == 0:
					foundinlist = 0
					for termtext, scoretext in words.iteritems():
    						if termtext == word:
							foundinlist = 1
					if foundinlist == 0:
						words[word] = 0
    			tweets[value] = sent
    #print "TWEEEEEEEETS"
    #for x, y in tweets.iteritems():
    	#print x,y
    #print "UNSCORED WORDS"
    #for a, b in words.iteritems():
    	#print a,b
    	
    for wrd, sen in words.iteritems():
   	cumsen = 0
   	count = 0
    	for twt, scr in tweets.iteritems():
    		for keywrd in twt.split():
    			if keywrd == wrd:
    				cumsen= cumsen + scr
    				count = count + 1
    	words[wrd] = cumsen/count
    
    for a, b in words.iteritems():
	print str(a)+"\t"+str(b)
   
    ''''						
    words = {} 
    for line in tweet_file:
    	data = json.loads(line)
	for key, value in data.iteritems() :
    		if key == "text":
    			#print value
    			sent = 0
    			misswordlist = {}
    			for word in value.split() :
    				foundinaddin = 0
    				for term, score in scores.iteritems():
    					if term == word:
    						sent = sent + score
    						foundinaddin = 1
    				if foundinaddin == 0:
    					misswordlist[word] = 0
    			
    			#print sent
    			for wrd, snt in misswordlist.iteritems():
    				temp = 0
    				for w,s in words.iteritems():
    					if w == wrd:
    						temp = s	
				words[wrd] = (snt + temp)/2
    for a, b in words.iteritems():
	print str(a)+"\t"+str(b)
    '''''
				
if __name__ == '__main__':
    main()
