def dict():
    res = {}
    f = open('cmudict.rep')
    for line in f.read().splitlines():
        if (line[0]) != '#':
            temp = []
            linesplit = line.split(' ', 1)
            syllables = linesplit[1].split('-')
            for syllable in syllables:
                temp.append(list(filter(None, syllable.split(' '))))
            res[linesplit[0]] = temp
    return res


def phonemes(phoneme_type):
    """
    :param phoneme_type: A string that is one of the following: vowel, stop, affricate, fricative, aspirate, liquid, nasal, semivowel or consonant
    :return: a dictionary containing all phonemes or, when specified only the required phoneme
    """
    phonemes = {
        'AA': 'vowel',
        'AE': 'vowel',
        'AH': 'vowel',
        'AO': 'vowel',
        'AW': 'vowel',
        'AY': 'vowel',
        'B': 'stop',
        'CH': 'affricate',
        'D': 'stop',
        'DH': 'fricative',
        'EH': 'vowel',
        'ER': 'vowel',
        'EY': 'vowel',
        'F': 'fricative',
        'G': 'stop',
        'HH': 'aspirate',
        'IH': 'vowel',
        'IY': 'vowel',
        'JH': 'affricate',
        'K': 'stop',
        'L': 'liquid',
        'M': 'nasal',
        'N': 'nasal',
        'NG': 'nasal',
        'OW': 'vowel',
        'OY': 'vowel',
        'P': 'stop',
        'R': 'liquid',
        'S': 'fricative',
        'SH': 'fricative',
        'T': 'stop',
        'TH': 'fricative',
        'UH': 'vowel',
        'UW': 'vowel',
        'V': 'fricative',
        'W': 'semivowel',
        'Y': 'semivowel',
        'Z': 'fricative',
        'ZH': 'fricative',
    }
    if (phoneme_type in phonemes.values()):
        return {k:v for k,v in phonemes.items() if v == phoneme_type}
    elif (phoneme_type == 'consonant'):
        return {k:v for k,v in phonemes.items() if v != 'vowel' and v != 'semivowel' and v!= 'aspirate'}
    else:
        return phonemes

if __name__ == '__main__':
    print(dict()['FRAMING'])