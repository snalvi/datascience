import sys

sentimentScores = {}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def parseSentimentScores(sent_file):
	for line in sent_file:
		


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
