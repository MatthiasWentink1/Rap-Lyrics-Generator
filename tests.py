import unittest
import syllable_matrices
import rhyme_detection as rd
import cmudict


class RhymeMatrixTestCase(unittest.TestCase):
    def setUp(self):
        self.consonants = syllable_matrices.consonant_matrix
        self.vowels = syllable_matrices.vowel_matrix

    def testConsonants(self):
        assert len(cmudict.phonemes('consonant')) == len(self.consonants)
        assert all([len(consonant) == len(cmudict.phonemes('consonant')) + 2 for consonant in self.consonants])

    def testVowels(self):
        assert len(cmudict.phonemes('vowel')) == len(self.vowels)
        assert all([len(vowel) == len(cmudict.phonemes('vowel')) for vowel in self.vowels])


class RhymeScoreTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def testRhymeScoreExample(self):
        # breaking vs checking is not checked explicitly as the splitting of syllables is done in a different way
        # assert rd.rhyme_score("the", "my") == -1.4, f"score was {rd.rhyme_score('the', 'my')}"
        # assert rd.rhyme_score("mold", "code") == 4.2, f"score was {rd.rhyme_score('mold', 'code')}"
        assert rd.rhyme_score("checking my code",
                              "breaking the mold") == 9.0, f"score was {rd.rhyme_score('checking my code', 'breaking the mold')}"

    def testStressScore(self):
        pass  # TODO make something

    def testConsonantScore(self):
        # assert rd.score_consonants(['K'], ['K']) == 2.6
        assert round(rd.score_consonants(['L', 'D'], ['D']), 2) == 1.35, f"was {rd.score_consonants(['L', 'D'], ['D'])}"

    def testSelfRhyme(self):
        pass
