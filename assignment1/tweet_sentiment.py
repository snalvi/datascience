import sys
import simplejson

sentimentScores = {}

def lines(fp):
    print str(len(fp.readlines()))

def parseSentimentScores(sent_file):
	for line in sent_file:
		wordSentScoreMapping = map(lambda x: x.strip(), line.split('\t'))
		sentimentScores[wordSentScoreMapping[0]] = int(wordSentScoreMapping[1])
	
def main():
    sent_file = open(sys.argv[1])
    parseSentimentScores(sent_file)

    tweet_file = open(sys.argv[2])

if __name__ == '__main__':
    main()
