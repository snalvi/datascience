import sys
import json
import re

sentimentScores = {}
frequencies = {}

totalWords = 0.0

def lines(fp):
    print str(len(fp.readlines()))
 
def calculateFrequency(word):
	if frequencies.has_key(word):
		frequencies[word] = frequencies[word] + 1.0
	else:
		frequencies[word] = 1.0

def parseWordsAndCalculateFrequencies(tweet_file):
	for line in tweet_file:
		# regex cleanup
		line = re.sub(r'(.*?:)false', r'\1"False"', line)
		line = re.sub(r'(.*?:)true', r'\1"True"', line)
		line = re.sub(r'(.*?:)null', r'\1""', line)

		tweetObj = json.loads(line)
		if tweetObj.has_key('text'):
			global totalWords	
			totalWords = len([calculateFrequency(word.strip()) for word in tweetObj['text'].encode('utf-8').split(' ')]) + totalWords


def printFrequencies():	
	for key in frequencies.keys():
		print key + ' ' + str(frequencies[key]/totalWords)

def main():
    tweet_file = open(sys.argv[1])
    parseWordsAndCalculateFrequencies(tweet_file)

    printFrequencies()


if __name__ == '__main__':
    main()
