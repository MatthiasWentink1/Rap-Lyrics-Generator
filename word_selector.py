import cmudict

cmu = cmudict.dict()


def count_syllables(word):
    return len(cmu[word.upper()])


def select_words(sentence, syllables):
    words = sentence.split(' ')
    res = [words[-1]]
    syllables -= count_syllables(words[-1])
    while syllables >= 0:
        for word in reversed(words):
            print(word)
    return res


if __name__ == '__main__':
    print(select_words("The house dead bolted with metal doors", 2))
