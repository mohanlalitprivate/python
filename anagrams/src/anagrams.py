from collections import Counter
import sys
import time


def read_words_from_file():
    with open('dictionary.txt', 'r') as file:
        return file.read().lower()


def get_user_input_word():
    user_input = input('>').lower()
    while not user_input.isalpha():
        print(f'Given input {user_input}, is not valid. Please use "exit" to end, or provide a valid alphabatic string')
        user_input = input(">")

    if user_input.lower() == 'exit':
        print(f'Thanks for trying.')
        sys.exit(0)
    else:
        return user_input


def find_anagrams(dictionary, user_word):
    #print(dictionary)
    #user_word_chars = list(user_word)
    #print(f'User word chars {user_word_chars}')
    user_word_char_count = Counter(user_word)
    print(f'Chars in word are {user_word_char_count}')
    found_anagrams = set()
    for dict_word in dictionary.split('\n'):
        #print(dict_word)
        if len(dict_word) == len(user_word) and set(dict_word) == set(user_word):

            print(dict_word)
            dic_word_char_count = Counter(dict_word)
            is_anagram = False
            for k, v in Counter(dict_word).items():
                print(f' k {k} ->  v {v}, user_word_char_count[k] {user_word_char_count[k]}')
                #print(f'')
                if v != user_word_char_count[k]:
                    is_anagram = False
                    break;
                else:
                    is_anagram = True
            if is_anagram:
                found_anagrams.add(dict_word)
    print(f'found anagrams {found_anagrams}')
    return found_anagrams


if __name__ == '__main__':
    start_time = time.time()
    dictionary = read_words_from_file()
    end_time = time.time()
    print(f"Dictionary loaded in {end_time - start_time} secs")
    word = get_user_input_word()
    find_anagrams(dictionary, word)

    sys.exit(0)
