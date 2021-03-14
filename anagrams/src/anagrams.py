from collections import Counter
import sys
import time


def read_words_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read().lower()
    except FileNotFoundError:
        print(f'Could not find file {file_name}, please check the file path')
        exit(-1)


def read_user_file(args):
    start_time = time.time()
    if len(args) != 2:
        print(f"To read anagrams this program takes exactly one argument for the file name to load")
        print(f"Example command 'python anagrams.py dictionary.txt")
        sys.exit(0)
    read_dictionary = read_words_from_file(sys.argv[1])
    end_time = time.time()
    print('Welcome to the Anagram finder')
    print('============================')
    print(f"Dictionary loaded in {end_time - start_time} milli secs")
    return read_dictionary


def get_user_input_word():
    user_input = input('>').lower()
    while not user_input.isalpha():
        print(f'Given input {user_input}, is not valid. Please use "exit" to end, or provide a valid alphabetic string')
        user_input = input(">")
    keep_prompting = True
    while keep_prompting:
        if user_input.lower() == 'exit':
            print(f'Thanks for trying.')
            keep_prompting = False
        elif not user_input.lower().isalpha():
            print(f'Given input {user_input}, is not valid. Please use "exit" to end, or provide a valid alphabetic string')
            user_input = input(">")
        else:
            print_anagrams_search_result(user_input)
            user_input = input('>').lower()


def print_anagrams_search_result(user_input):
    search_start_time = time.time()
    found_anagrams = find_anagrams(_read_dictionary, user_input)
    if len(found_anagrams) != 0:
        print(f'{len(found_anagrams)} anagrams found for "{user_input}" in {time.time() - search_start_time} milli secs')
        anagrams_as_str = ', '.join(e for e in found_anagrams)
        print(anagrams_as_str)
        found_anagrams.clear()
    else:
        print(f'No anagrams found for "{user_input}"')


def find_anagrams(dictionary_words, user_word):
    user_word_char_count = Counter(user_word)
    found_anagrams = set()
    for dict_word in dictionary_words.split('\n'):
        dict_word = dict_word.strip()
        if len(dict_word) == len(user_word) and set(dict_word) == set(user_word):
            is_anagram = True
            for k, v in Counter(dict_word).items():
                #print(f' k {k} ->  v {v}, user_word_char_count[k] {user_word_char_count[k]}')
                if v != user_word_char_count[k]:
                    is_anagram = False
                    break;
            if is_anagram:
                found_anagrams.add(dict_word)
    return found_anagrams


if __name__ == '__main__':
    global _read_dictionary
    _read_dictionary = read_user_file(sys.argv)
    get_user_input_word()
    sys.exit(0)
