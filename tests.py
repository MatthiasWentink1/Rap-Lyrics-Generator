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
        test_score = rd.rhyme_score("testing","best thing")
        assert test_score == 4.8, f"score was {test_score}"

    def testConsonantScore(self):
        assert round(rd.score_consonants(['L', 'D'], ['D']), 2) == 1.35, f"was {rd.score_consonants(['L', 'D'], ['D'])}"
