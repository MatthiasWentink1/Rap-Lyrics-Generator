import cmudict

cmu = cmudict.dict()


def count_syllables(word):
    if word.upper() in cmu:
        return len(cmu[word.upper()])
    else:
        return 1.66 #TODO dit globaal ergens defineren


def is_interesting(word):
    uninteresting = ["the", "i", "my", "and", "to", "this", "is"]
    return word.lower() not in uninteresting and word.upper() in cmu.keys()


def select_words(sentence, syllables):
    words = sentence.split(' ')
    res = []
    for i in range(len(words)):
        if is_interesting(words[i]):
            counted_syllables = count_syllables(words[i])
            if syllables - counted_syllables >= 0:
                res.append(i)
                syllables -= counted_syllables
    res.append(len(words) -1)
    return res


if __name__ == '__main__':
    print(select_words("The house dead bolted with metal doors", 2))
