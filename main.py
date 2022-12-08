# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

import cmudict
from syllable_matrices import vowel_matrix, consonant_matrix

cmu_vowels = [a for (a, b) in cmudict.phones() if b == ['vowel']]
cmu_consonants = [a for (a, b) in cmudict.phones() if b != ['vowel'] and b != ['aspirate'] and b != ['semivowel']]


def sentence_to_syllables(sentence):
    words = sentence.split(" ")
    res = cmudict.dict()[words[0]][0]
    for word in words[1:]:
        res.extend(cmudict.dict()[word][0])
    return res


def get_phone_type(input_phone):
    for (phone, type) in cmudict.phones():
        if input_phone == phone:
            return type[0]


def get_rhyme_score(a, b):
    if a in cmu_vowels and b in cmu_vowels:
        a_index = cmu_vowels.index(a)
        b_index = cmu_vowels.index(b)
        if a_index > b_index:
            a_index, b_index = b_index, a_index
        return vowel_matrix[a_index][b_index]
    elif a in cmu_consonants and b in cmu_consonants:
        a_index = cmu_consonants.index(a)
        b_index = cmu_consonants.index(b)
        if a_index > b_index:
            a_index, b_index = b_index, a_index
        return consonant_matrix[a_index][b_index]
    else:
        raise Exception("Inputs are not of the same type")

# The final score for two given syllables is the sum of the vowel score, normalized consonant score, and stress score.
def get_syllables(word):
    phones = cmudict.dict()[word][0]
    print(phones)
    vowel_detected = False
    res = []
    temp = []
    consonants = []
    i = 0
    while i < len(phones):
        print(f'i: {i}, phone: {phones[i]}')
        if get_phone_type(phones[i][0:2]) == 'vowel':
            if vowel_detected:
                half = math.ceil(len(consonants)/2)
                temp.extend(consonants[0:half])
                res.append(temp)
                print(half)
                i = i - (half)
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
    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_syllables("pandemonium"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
