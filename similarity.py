import logging
import numpy as np
from scipy import spatial
from pprint import pprint as print
from gensim.models.fasttext import FastText
from gensim.test.utils import datapath
import pickle

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import gensim.downloader as api

wv = api.load('fasttext-wiki-news-subwords-300')


def corpus_to_ngram(corpus, n):
    """
    :param corpus: A corpus file
    :param n: Size of the N-gram
    :return: List of word lists of size n
    """
    n_grams = []
    i = 0
    for line in corpus.read().splitlines():
        i += 1
        if len(line) > 0:
            words = line.split(" ")
            for i in range(len(words) - n + 1):
                n_grams.append(tuple([words[j] for j in range(i, i + n)]))
    return n_grams


def ngrams_similarity_score(ngrams):
    """
    Calculates the similarity score of a list of N-grams
    :param ngrams: list of N-grams
    :return: a dict with the N-gram as key and the mean word vector for the N-gram as value
    """
    res = {}
    for ngram in ngrams:
        res[ngram] = np.mean([wv[word] for word in ngram if word in wv], axis=0)
    return res


# TODO similarity_scores is a vague term, name functions better

def word_similarity(word, similarity_scores, filter=0):
    """
    calculates the distance between a word and all the words in a similarity score dictionary
    :param word: String
    :param similarity_scores: Dictionary of N-grams and their vectors
    :return:
    """
    res = {}
    word_vector = wv[word]
    for (key, value) in similarity_scores.items():
        try:
            res[key] = 1 - spatial.distance.cosine(word_vector, value)
        except:
            print(f"key: {key}")
    res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
    return {k:v for (k,v) in res.items() if v > filter}


if __name__ == '__main__':
    with open('dataset3-processed.txt', 'r') as f:
        tri_grams = corpus_to_ngram(f, 3)
        similarity = ngrams_similarity_score(tri_grams)

    # with open('wiki_dump.txt','wb') as f:
    #     pickle.dump(similarity, f, protocol=pickle.HIGHEST_PROTOCOL)

    # with open('wiki_dump.txt', 'rb') as f:
    #     similarities = pickle.load(f)
    #     words = word_similarity('bird', similarities, 0.85)
    #     print(words)
    #     i = 0
