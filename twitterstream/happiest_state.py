import sys
import json



def main():
    tweet_file = open(sys.argv[1])
    states = {"AL": 0,"AK": 0,"AZ": 0, "AR": 0, "CA" : 0, "CO": 0, "CT": 0, "DE":0, "FL":0, "GA":0, "HI": 0, "ID": 0, "IL": 0, "IN": 0, "IA": 0, "KS": 0, "KY": 0, "LA": 0,   "ME": 0, "MD": 0, "MA": 0, "MI": 0, "MN": 0, "MS": 0, "MO": 0, "MT": 0, "NE": 0, "NV": 0, "NH": 0, "NJ": 0, "NM": 0, "NY": 0, "NC": 0, "ND": 0,"OH": 0, "OK": 0, "OR": 0, "PA": 0, "RI": 0, "SC": 0, "SD": 0, "TN": 0, "TX": 0, "UT": 0, "VT": 0, "VA": 0, "WA": 0, "WV": 0, "WI": 0, "WY": 0}
    sent_file = open(sys.argv[2])
    scores = {}
    for line in tweet_file:
    		term, score  = line.split("\t")
		scores[term] = int(score) 		 
    for line in sent_file:
    	data = json.loads(line)
	for key, value in data.iteritems() :
    		if key == "text":
    			sent = 0
    			for word in value.split() : 
    				for term, score in scores.iteritems():
    					if term == word:
    						sent = sent + score

    			if sent > 0:
    				for key1, value1 in data.iteritems() :
    					if key1 == "user":
    						loc = value1["location"]
						if len(loc) > 2:
							st = (loc[len(loc) - 2]+loc[len(loc) - 1]).upper()
							for stt, stcnt in states.iteritems():
    								if (st == stt):
    									states[st] = states[st] + 1
    maxcount = 0
    maxstate = "AL"
    for state, count in states.iteritems() :	
    	if count > maxcount:
    		maxcount = count
    		maxstate = state

    print maxstate
	
if __name__ == '__main__':
    main()
