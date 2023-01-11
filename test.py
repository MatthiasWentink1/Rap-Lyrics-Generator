import cmudict
import rhyme_detection as rd
from transformers import BertTokenizer, BertForMaskedLM
import random
import torch
import similarity


tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForMaskedLM.from_pretrained("bert-base-uncased")


def select_rhyme_words(input_word):
    rhyming_words = []
    for word in cmudict.dict().keys():
        try:
            rhyming_words.append((word, rd.rhyme_score(input_word, word)))
        except:
            pass
    rhyming_words.sort(key=lambda x: x[1], reverse=True)

    chosen_word = ("", 0)
    for rhyme_word in rhyming_words[:10]:
        word = rhyme_word[0]
        try:
            print(word)
            print(input_word)
            if word != input_word:
                similarity_score = similarity.wv.similarity(word.lower(), input_word.lower())
            else:
                similarity_score = 0
        except KeyError:
            similarity_score = 0
        if similarity_score > chosen_word[1]:
            chosen_word = (word, similarity_score)
    return chosen_word


def generate_mask(sentence, rhyme_words):
    sentence_split = sentence.split(" ")
    for word in rhyme_words:
        if not word in sentence_split:
            pass
    rhymed_words = [select_rhyme_words(word) for word in rhyme_words]
    masked_sentence = ["[MASK]"] * len(sentence_split)
    for i in range(len(sentence_split)):
        if sentence_split[i] in rhyme_words:
            masked_sentence[i] = rhymed_words[rhyme_words.index(sentence_split[i])][0]
    sentence_split.append("[SEP]")
    sentence_split.extend(masked_sentence)
    return ' '.join(sentence_split)


def fill_mask(masked_sentence):
    inputs = tokenizer(masked_sentence, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits

    # retrieve index of [MASK]
    mask_token_index = (inputs.input_ids == tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]

    predicted_token_id = logits[0, mask_token_index].argmax(axis=-1)
    i, j = 0, 0
    bert_words = tokenizer.batch_decode(predicted_token_id)
    print(bert_words)
    result = masked_sentence.split()
    for word in masked_sentence.split():
        if word == "[MASK]":
            result[i] = bert_words[j]
            i += 1
            j += 1
        else:
            i += 1
    return format_result(' '.join(result))


def format_result(sentence):
    return sentence.lower().replace("[sep] ", "\n")


if __name__ == '__main__':
    input_words = "today i will win"
    rhyme_words = ["today", "will"]
    print(fill_mask(generate_mask(input_words, rhyme_words)))