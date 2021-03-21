from collections import Counter


def find_anagrams(dictionary_words, user_word):
    user_word_char_count = Counter(user_word)
    found_anagrams = set()
    for dict_word in dictionary_words.split('\n'):
        dict_word = dict_word.strip()
        if len(dict_word) == len(user_word) and set(dict_word) == set(user_word):
            is_anagram = True
            for k, v in Counter(dict_word).items():
                if v != user_word_char_count[k]:
                    is_anagram = False
                    break;
            if is_anagram:
                found_anagrams.add(dict_word)
    return found_anagrams
