import sys
import json
import re

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

		# regex cleanup
		line = re.sub(r'(.*?:)false', r'\1"False"', line)
		line = re.sub(r'(.*?:)true', r'\1"True"', line)
		line = re.sub(r'(.*?:)null', r'\1""', line)

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
