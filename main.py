# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import itertools

import cmudict
from syllable_matrices import vowel_matrix, consonant_matrix

cmu_vowels = [a for (a, b) in cmudict.phones() if b == ['vowel']]
cmu_consonants = [a for (a, b) in cmudict.phones() if b != ['vowel'] and b != ['aspirate'] and b != ['semivowel']]


def sentence_to_syllables(sentence):
    """
    :param sentence: String of text
    :return: the phones in that text
    """
    words = sentence.split(" ")
    res = cmudict.dict()[words[0]][0]
    for word in words[1:]:
        res.extend(cmudict.dict()[word][0])
    return res


def get_phone_type(input_phone):
    """
    :param input_phone: String containing capitalized characters that resemble an phoneme in the Arpanet
    :return: type of phoneme
    """
    for (phone, type) in cmudict.phones():
        if input_phone == phone:
            return type[0]


def rhyme_score(phoneme_1, phoneme_2):
    """
    Look up function for the rhyme score of two phonemes given that they are either both vowels or both consonants
    :param phoneme_1: a phoneme according to Arpanet
    :param phoneme_2: a phoneme according to Arpanet
    :return: the corresponding rhyme score of the two phonemes
    """
    if phoneme_1 in cmu_vowels and phoneme_2 in cmu_vowels:
        a_index = cmu_vowels.index(phoneme_1)
        b_index = cmu_vowels.index(phoneme_2)
        if a_index > b_index:
            a_index, b_index = b_index, a_index
        return vowel_matrix[a_index][b_index]
    elif phoneme_1 in cmu_consonants and phoneme_2 in cmu_consonants:
        a_index = cmu_consonants.index(phoneme_1)
        b_index = cmu_consonants.index(phoneme_2)
        if a_index > b_index:
            a_index, b_index = b_index, a_index
        return consonant_matrix[a_index][b_index]
    else:
        raise Exception("Inputs are not of the same type")


def get_syllables(word):
    """ An algorithm that groups the phonemes of an input word into syllables
    :param word:
    :return: A list of phoneme lists
    """
    phones = cmudict.dict()[word][0]
    vowel_detected = False
    res = []
    temp = []
    consonants = []
    i = 0
    while i < len(phones):
        if get_phone_type(phones[i][0:2]) == 'vowel':
            if vowel_detected:
                half = math.ceil(len(consonants) / 2)
                temp.extend(consonants[0:half])
                res.append(temp)
                i = i - (half + 1)
                temp = []
                consonants = []
                vowel_detected = False
            else:
                temp.append(phones[i])
                vowel_detected = True
        else:
            if vowel_detected:
                consonants.extend(phones[i])
            else:
                temp.extend(phones[i])
        i = i + 1
    temp.extend(consonants)
    res.append(temp)
    for i in range(0, len(res) - 1):
        if res[i][len(res[i]) - 1] == res[i + 1][0]:
            cut = len(res[i]) - 1
            res[i] = res[i][0:cut]
    return res


def syllable_score(syllable_1, syllable_2):
    """
    :param syllable_1: a group of phonemes
    :param syllable_2: a group of phonemes
    return the rhyme score for both syllables according to the formula: TODO
    """
    vowel_position_1, vowel_position_2 = vowel_position(syllable_1), vowel_position(syllable_2)
    vowel_score = rhyme_score(syllable_1[vowel_position_1][0:2], syllable_2[vowel_position_2][0:2])
    stress_score = int(syllable_1[vowel_position_1][2]) + int(syllable_2[vowel_position_2][2])
    consonant_score = 0
    consonants_1, consonants_2 = [], []
    if len(syllable_1) != vowel_position_1:
        consonants_1 = syllable_1[vowel_position_1 + 1: len(syllable_1)]
    if len(syllable_2) != vowel_position_2:
        consonants_2 = syllable_2[vowel_position_2 + 1: len(syllable_2)]
    paired_consonants = itertools.zip_longest(consonants_1, consonants_2)
    print(list(paired_consonants))
    for pair in list(paired_consonants):
        if pair[0] is None:
            print('a')
            consonant_score += consonant_matrix[cmu_consonants.index(pair[1])][21]
        elif pair[1] is None:
            print('b')
            consonant_score += consonant_matrix[cmu_consonants.index(pair[0])][21]
        else:
            consonant_score += rhyme_score(pair[0], pair[1])

    if (max(len(consonants_1), len(consonants_2)) > 0):
        consonant_score = consonant_score / max(len(consonants_1), len(consonants_2))

    return vowel_score + stress_score + consonant_score
    # coda in front of nucleus


def vowel_position(syllable):
    """
    :param syllable: list of phonemes
    :return: the index at which the vowel is located
    """
    for i in range(0, len(syllable)):
        if get_phone_type(syllable[i][0:2]) == 'vowel':
            return i
    return 0


if __name__ == '__main__':
    rain = get_syllables('tree')
    frame = get_syllables('tree')
    print(rain)
    print(frame)
    print(syllable_score(rain[0], frame[0]))

# NOTES
# The final score for two given syllables is the sum of the vowel score, normalized consonant score, and stress score.
# This version of CMU has semivowels which are not included into the research by Hirjee
# What is the threshold for a rhyme?
# How is stress score calculated?
# Which unmatched thing should I take? For now I just use the same thing
# Is this way of getting syllables good enough?
# How will I do the alignment
