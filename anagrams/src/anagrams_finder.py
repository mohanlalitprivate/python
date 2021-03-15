from collections import Counter


def read_words_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read().lower()
    except FileNotFoundError:
        print(f'Could not find file {file_name}, please check the file path')
        exit(-1)


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
