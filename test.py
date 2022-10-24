import pke
import sys
sys.path.append('./SentimentAnalysis')

from SentimentAnalysis.output import sentiment_score
def keyword_extraction(input):
    # initialize keyphrase extraction model, here TopicRank
    extractor = pke.unsupervised.TopicRank()

    # load the content of the document, here document is expected to be a simple 
    # test string and preprocessing is carried out using spacy
    extractor.load_document(input=input, language='en')

    # keyphrase candidate selection, in the case of TopicRank: sequences of nouns
    # and adjectives (i.e. `(Noun|Adj)*`)
    extractor.candidate_selection()

    # candidate weighting, in the case of TopicRank: using a random walk algorithm
    extractor.candidate_weighting()

    # N-best selection, keyphrases contains the 10 highest scored candidates as
    # (keyphrase, score) tuples
    keyphrases = extractor.get_n_best(n=10)
    output = [t[0] for t in keyphrases]
    return output

def request_sentiment(input):
    return sentiment_score(input)


def request_sentiment_keywords(input):
    sentiment, percentage = sentiment_score(input)
    keywords = keyword_extraction(input)
    s = ''.join(sentiment)
    s = s +" "+ str(percentage)
    s1 = ''.join(str(x) for x in keywords)
    s = s+" "+s1
    return s

def request_keywords(input):
    return keyword_extraction(input)

