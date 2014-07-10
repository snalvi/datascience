import sys
import json
import re

knownSentimentScores = {}
unknownSentimentScores = {}

def lines(fp):
    print str(len(fp.readlines()))

def parseSentimentScores(sent_file):
    for line in sent_file:
        wordSentScoreMapping = [word.strip() for word in line.split('\t')]
        knownSentimentScores[wordSentScoreMapping[0]] = float(wordSentScoreMapping[1])
 
def calculateSentiments(tweet_file):
    for line in tweet_file:

        # regex cleanup
        line = re.sub(r'(.*?:)false', r'\1"False"', line)
        line = re.sub(r'(.*?:)true', r'\1"True"', line)
        line = re.sub(r'(.*?:)null', r'\1""', line)

        tweetObj = json.loads(line)
        tweetSentimentScore = 0.0

        if tweetObj.has_key('text'):

            tweetWordsArray = tweetObj['text'].encode('utf-8').split(' ')

            #overall summation of words thus far
            tweetSentimentScore = sum(map(lambda word: knownSentimentScores[word] if knownSentimentScores.has_key(word) else 0.0, tweetWordsArray))

            #now we need to calculate the sentiment score of words not in the known sentiments
            for word in tweetWordsArray:
                if not knownSentimentScores.has_key(word):
                    unknownWordSentiment = 0.0
                    totalWords = float(len(tweetWordsArray))

                    try:
                        unknownWordSentiment = unknownSentimentScores[word]
                        totalWords += 1.0
                    except KeyError:
                        unknownWordSentiment = 0.0

                    newSentimentScore = (tweetSentimentScore + unknownWordSentiment) / totalWords
                    unknownSentimentScores[word] = newSentimentScore


def outputSentimentScores():

    for key in unknownSentimentScores.keys():
        print key + ' ' + str(unknownSentimentScores[key])

def main():
    sent_file = open(sys.argv[1])
    parseSentimentScores(sent_file)

    tweet_file = open(sys.argv[2])
    calculateSentiments(tweet_file)

    outputSentimentScores()

if __name__ == '__main__':
    main()
