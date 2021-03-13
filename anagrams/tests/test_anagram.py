from unittest import TestCase
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from src import anagrams


class AnagramTestCase(TestCase):
    def setUp(self):
        # setuptest here
        self.dictionary = 'post\n opts\nstop\ntops\napple\norange\ntest\n'

    def test_find_anagrams(self):
        returned_anagrams = anagrams.find_anagrams(self.dictionary, "stop")
        self.assertEqual({'stop', 'tops', 'post'}, returned_anagrams)

