import sys
import json

hashtagFrequencies = {}
topTenHashtags = {}

TOP_HASHTAG_AMOUNT = 10

def lines(fp):
    print str(len(fp.readlines()))
 
def addHashtagFrequency(hashtag):
	if hashtagFrequencies.has_key(hashtag):
		hashtagFrequencies[hashtag] += 1.0
	else: 
		hashtagFrequencies[hashtag] = 1.0

def parseHashtagsAndCalculateFrequencies(tweet_file):
	for line in tweet_file:

		global totalWordCount

		line = line.encode('utf-8')
		tweetObj = json.loads(line)

		if tweetObj.has_key('entities') and tweetObj['entities'].has_key('hashtags'):
			hashtags = tweetObj['entities']['hashtags']

			if len(hashtags) != 0:
				 [addHashtagFrequency(hashtagObj['text'].lower().strip()) for hashtagObj in hashtags]


def getTopHashtag():
	topHashtag = max(hashtagFrequencies.iterkeys(), key=(lambda key: hashtagFrequencies[key]))
	topTenHashtags[topHashtag] = hashtagFrequencies[topHashtag]
	del(hashtagFrequencies[topHashtag])


#pull out top 10 hashtags first
#print those
def printTopTenTags():
	while (len(topTenHashtags) < TOP_HASHTAG_AMOUNT) and (len(hashtagFrequencies) > 0):
		getTopHashtag()

	for hashtag in topTenHashtags.keys():
		print hashtag + ' ' + str(topTenHashtags[hashtag])

def main():
    tweet_file = open(sys.argv[1])
    parseHashtagsAndCalculateFrequencies(tweet_file)

    printTopTenTags()

if __name__ == '__main__':
    main()
