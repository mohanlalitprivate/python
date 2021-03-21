import sys
import time
import anagrams_loader, user_interaction


def read_user_file(args):
    if len(args) != 2:
        print(f'To read anagrams this program takes exactly one argument for the file name to load')
        print(f'Example command "python anagrams.py dictionary.txt"')
        sys.exit(0)
    start_time = time.process_time()  # changed this to use new recommendations
    read_dictionary = anagrams_loader.read_words_from_file(sys.argv[1])
    time_taken = time.process_time() - start_time
    print('Welcome to the Anagram finder')
    print('============================')
    print(f"Dictionary loaded in {time_taken/100} rounded {round(time_taken, 6)} secs")
    return read_dictionary


if __name__ == '__main__':
    user_interaction.find_anagrams_for_user_input(read_user_file(sys.argv))
    sys.exit(0)

