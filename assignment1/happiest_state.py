import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

sentimentScores = {}
stateSentimentScores = {}
numTweets = 0

def getStateCodeGivenState(state):
	for stateCode in states.keys():
		if states[stateCode] == state:
			return stateCode

	return ''

def calculateSentimentForTweetFromState(tweet, state):
	tweetSentimentScore = sum(map(lambda word: sentimentScores[word] if sentimentScores.has_key(word) else 0, tweet.split(' ')))
	
	if stateSentimentScores.has_key(state):
		stateSentimentScores[state] = stateSentimentScores[state] + tweetSentimentScore
	else:
		stateSentimentScores[state] = tweetSentimentScore

	global numTweets
	numTweets += 1

def parseSentimentScores(sent_file):
	for line in sent_file:
		wordSentScoreMapping = [word.strip() for word in line.split('\t')]
		sentimentScores[wordSentScoreMapping[0]] = int(wordSentScoreMapping[1])
 
def determineStateByCoordinates(coordinates):
	return ''

def determineStateByPlace(place):
	return '' 

def parseTweetsForHappiestState(tweet_file):
	for line in tweet_file:

		line = line.encode('utf-8')
		tweetObj = json.loads(line)
		
		if tweetObj.has_key('text'):
			state = ''
			if tweetObj.has_key('coordinates'):
				state = determineStateByCoordinates(tweetObj['coordinates'])

			if state == '' and tweetObj.has_key('place'):
				state = determineStateByPlace(tweetObj['place'])

			if state == '' and tweetObj.has_key('user'):
				state = determineStateByUser(tweetObj['user'])

			if state != '':
				calculateSentimentForTweetFromState(tweetObj['text'], state)
		else: 
			pass

#get highest sum from dictionary at the end; divide by total number of tweets
def printHappiestState():
	print "Saman"

def main():
    sent_file = open(sys.argv[1])
    parseSentimentScores(sent_file)

    tweet_file = open(sys.argv[2])
    parseTweetsForHappiestState(tweet_file)

if __name__ == '__main__':
    main()
