# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import itertools
import cmudict

from syllable_matrices import vowel_matrix, consonant_matrix

cmu_vowels = list(cmudict.phonemes('vowel').keys())
cmu_consonants = list(cmudict.phonemes('consonant').keys())
cmu_dict = cmudict.dict()


def phoneme_score(phoneme_1, phoneme_2):
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


def score_stress(stress_1, stress_2):
    if stress_1 == stress_2:  # The same stress scores
        if stress_1 == 1:
            return 2
        elif stress_1 == 2:
            return 1
    elif stress_1 > 0 and stress_2 > 0:  # Not the same stress but one stressed
        return 0.5
    return 0  # Not the same stress and none stressed


def syllable_score(syllable_1, syllable_2):
    """
    :param syllable_1: a group of phonemes
    :param syllable_2: a group of phonemes
    return the rhyme score for both syllables according to the formula: TODO
    """
    vowel_position_1, vowel_position_2 = vowel_position(syllable_1), vowel_position(syllable_2)
    vowel_score = phoneme_score(syllable_1[vowel_position_1][0:2], syllable_2[vowel_position_2][0:2])
    stress_score = score_stress(int(syllable_1[vowel_position_1][2]), int(syllable_2[vowel_position_2][2]))
    consonant_score = 0
    consonants_1, consonants_2 = [], []
    if len(syllable_1) != vowel_position_1:
        consonants_1 = syllable_1[vowel_position_1 + 1: len(syllable_1)]
    if len(syllable_2) != vowel_position_2:
        consonants_2 = syllable_2[vowel_position_2 + 1: len(syllable_2)]
    paired_consonants = itertools.zip_longest(consonants_1, consonants_2)
    for pair in list(paired_consonants):
        if pair[0] is None:
            consonant_score += consonant_matrix[cmu_consonants.index(pair[1])][21]
        elif pair[1] is None:
            consonant_score += consonant_matrix[cmu_consonants.index(pair[0])][21]
        else:
            consonant_score += phoneme_score(pair[0], pair[1])

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
        if cmudict.phonemes('')[syllable[i][0:2]] == 'vowel':
            return i
    return 0


def sentence_to_syllables(sentence):
    res = []
    for word in sentence.split(' '):
        res.extend(cmu_dict[word.upper()])
    return res


def rhyme_score(sentence_1, sentence_2):
    score = 0
    sentence_1, sentence_2 = sentence_1.upper(), sentence_2.upper()
    syllables_1, syllables_2 = sentence_to_syllables(sentence_1), sentence_to_syllables(sentence_2)
    if len(syllables_1) == len(syllables_2):
        for i in range(len(syllables_1)):
            score += syllable_score(syllables_1[i], syllables_2[i])
    else:
        raise Exception("Inputs are not of the same type")
    return score


if __name__ == '__main__':
    score = rhyme_score('bend', 'wind')
    print(score)

# NOTES
# The final score for two given syllables is the sum of the vowel score, normalized consonant score, and stress score.
# This version of CMU has semivowels which are not included into the research by Hirjee
# How is stress score calculated?
# Which unmatched thing should I take? For now I just use the same thing
