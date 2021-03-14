from unittest import TestCase
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from src import anagrams


class AnagramTestCase(TestCase):
    def setUp(self):
        # setup test here
        anagram_list = ['spot', 'post',' stop',' tops',' stopp',' topss',' spoot',' nstop',' stnp',]
        #self.anagram_exists = 'spot\npost\n opts\nstop\ntops\nstopp\ntopss\nspoot\nnstop\nstnp\n'
        self.anagram_exists = ('\n'.join(a for a in anagram_list))

    def test_find_anagrams(self):
        returned_anagrams = anagrams.find_anagrams(self.anagram_exists, "stop")
        self.assertEqual({'stop', 'tops', 'post', 'spot'}, returned_anagrams)
        self.assertEqual(set(), anagrams.find_anagrams(self.anagram_exists, "stopper"))
        self.assertEqual(set(), anagrams.find_anagrams(self.anagram_exists, "sto"))
        self.assertEqual({'stopp'}, anagrams.find_anagrams(self.anagram_exists, "stopp"))
        self.assertEqual(set(), anagrams.find_anagrams(self.anagram_exists, "s"))
        self.assertEqual(set(), anagrams.find_anagrams(self.anagram_exists, ""))
