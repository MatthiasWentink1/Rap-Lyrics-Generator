# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_rhyme_score('ZH', 'CH'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
