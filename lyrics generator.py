import gensim.downloader as api

import pickle

import numpy as np
from scipy import spatial

import cmudict
import rhyme_detection as rd
import word_selector as ws
from transformers import BertTokenizer, BertForMaskedLM
import timeit
import torch

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForMaskedLM.from_pretrained("bert-base-uncased")
wv = api.load('word2vec-google-news-300')
cmu = cmudict.dict()
syllables_per_word = 1.66

with open('two_tuples.txt', 'rb') as f:
    similarity = pickle.load(f)
    ngrams = [' '.join(words) for words in similarity.keys()]

with open('bad-words.txt', 'r') as bw:
    bad_words = bw.read().splitlines()


def generate_mask_syllables(sentence, rhyme_indexes):
    split_sentence = sentence.split()
    rhymed_words = select_rhyme_words([split_sentence[i] for i in rhyme_indexes])
    padded_indexes = list(set([0] + rhyme_indexes + [len(split_sentence)]))
    syllable_intervals = []
    for i in range(len(padded_indexes) - 1):
        index_a, index_b = padded_indexes[i], padded_indexes[i + 1]
        if index_a in rhyme_indexes:
            syllable_intervals.append((index_a, index_a))
            syllable_intervals.append((index_a + 1, index_b))
        else:
            syllable_intervals.append((index_a, index_b))
    syllable_intervals = list(dict.fromkeys(syllable_intervals))[0:-1]
    generator_template = [
        round(
            sum([ws.count_syllables(split_sentence[i]) / syllables_per_word for i in range(interval[0], interval[1])]))
        for interval in syllable_intervals]
    rhymed_word_index = 0
    result = []
    for x in generator_template:
        if x > 0:
            result.extend(["[MASK]"] * x)
        else:
            result.extend(rhymed_words[rhymed_word_index][0])
            rhymed_word_index += 1
    result = " ".join(split_sentence + ["[SEP]"] + result + ["."])
    return result

def vector_ngram(ngram):
    word_vectors = []
    for word in ngram.split():
        try:
            word_vectors.append(wv[word.lower()])
        except KeyError:
            pass
    return np.mean(word_vectors, axis=0)


def spatial_distance(a, b):
    try:
        score = 1 - spatial.distance.cosine(a[2], b[2])
        return score
    except ValueError:
        # If there are faulty words in the ngrams that do not have a word-vector. Disregard them
        return 0


def is_profane(word):
    return word in bad_words


def select_rhyme_words(words_to_rhyme, profanity_allowed=False):
    rhymed_words = []
    for word in words_to_rhyme:
        result = []
        # word_vector = wv[word]
        for ngram in ngrams:
            try:
                chosen_rhyme = rd.sliding_window(word, ngram)
                chosen_rhyme_words = rd.words_from_syllables(chosen_rhyme[0], ngram)
                if profanity_allowed or not any(
                        [is_profane(chosen_rhyme_word) for chosen_rhyme_word in chosen_rhyme_words]):
                    result.append((chosen_rhyme_words, chosen_rhyme[1], similarity[tuple(ngram.split())]))
            except KeyError:
                pass
            except:
                pass
                # print(ngram)
        if len(rhymed_words) > 0:
            try:
                selected_word = max(filter(lambda x: x[1] > 3, result),
                                    key=lambda x: spatial_distance(x, rhymed_words[-1]))
                rhymed_words.append(selected_word)
            except ValueError:
                # Could not find a well enough rhyme
                rhymed_words.append("[MASK]")
        else:
            try:
                selected_word = max(filter(lambda x: x[1] > 3, result), key=lambda x: x[1])
                rhymed_words.append(selected_word)
            except ValueError:
                # Could not find a well enough rhyme
                rhymed_words.append("[MASK]")
    print([(" ".join(rhymed_words[i][0]), words_to_rhyme[i]) for i in range(len(rhymed_words))])
    return rhymed_words


def fill_mask(masked_sentence):
    inputs = tokenizer(masked_sentence, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    mask_token_index = (inputs.input_ids == tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]
    predicted_token_id = logits[0, mask_token_index].argmax(axis=-1)
    j = 0
    fill_words = tokenizer.decode(predicted_token_id).split(" ") + (["-"] * 10)
    result = masked_sentence.split()
    for i in range(len(result)):
        if result[i] == '[SEP]':
            result[i] = '\n'
        elif result[i] == '[MASK]':
            result[i] = fill_words[j]
            j += 1
    return result


def generate_lyrics(input_words):
    words_to_rhyme_index = ws.select_words(input_words, 3)
    words_to_rhyme = [input_words.split()[index] for index in words_to_rhyme_index]
    return fill_mask(generate_mask_syllables(input_words, words_to_rhyme_index))

if __name__ == "__main__":
    start = timeit.default_timer()

    with open('intros.txt') as songtext:
        songtext_lines = songtext.read().splitlines()

    for line in songtext_lines:
        print(" " + " ".join(generate_lyrics(line)) + "\n")

    stop = timeit.default_timer()
    print('Time: ', stop - start)