import sys
import simplejson
import json

sentimentScores = {}

def lines(fp):
    print str(len(fp.readlines()))

def parseSentimentScores(sent_file):
	for line in sent_file:
		# wordSentScoreMapping = map(lambda x: x.strip(), line.split('\t'))
		wordSentScoreMapping = [word.strip() for word in line.split('\t')]
		sentimentScores[wordSentScoreMapping[0]] = int(wordSentScoreMapping[1])
 
def calculateSentiments(tweet_file):
	for line in tweet_file:

		#cleaning data
		line = line.replace('false', '\"False\"')
		line = line.replace('true', '\"True\"')
		line = line.replace(':null', ':\"\"')

		tweetObj = json.loads(line)
		if tweetObj.has_key('text'):
			wordScores = map(lambda word: sentimentScores[word] if sentimentScores.has_key(word) else 0, tweetObj['text'].split(' '))
			print sum(wordScores) #for readability

		else: #no tweet text; so by default the sentiment is nothing
			print 0

def main():
    sent_file = open(sys.argv[1])
    parseSentimentScores(sent_file)

    tweet_file = open(sys.argv[2])
    calculateSentiments(tweet_file)

if __name__ == '__main__':
    main()
