import sys
import time
import anagrams_finder


def find_anagrams_for_user_input(_read_dictionary):
    while True:
        user_input = input('>').lower()
        '''
        print(f'permutations {permutations(user_input)}')
        for i in user_input:
            print(permutations(i))

        for i in permutations(user_input):
            print(i)
        '''
        if user_input.lower() == 'exit':
            print(f'Thanks for trying.')
            break
        elif not user_input.lower().isalpha():
            print(
                f'Given input {user_input}, is not valid. Please use "exit" to end, '
                f'or provide a valid alphabetic string')
        else:
            print_anagrams_search_result(user_input, _read_dictionary)


def print_anagrams_search_result(user_input, _read_dictionary):
    search_start_time = time.process_time() # changed to process time
    found_anagrams = anagrams_finder.find_anagrams(_read_dictionary, user_input)
    if len(found_anagrams) != 0:
        print(f'{len(found_anagrams)} anagrams found for "{user_input}" in '
              f'{round(time.process_time() - search_start_time, 6)} milli secs')
        anagrams_as_str = ', '.join(e for e in found_anagrams)
        print(anagrams_as_str)
        found_anagrams.clear()
    else:
        print(f'No anagrams found for "{user_input}"')

