
def read_words_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read().lower()
    except FileNotFoundError:
        print(f'Could not find file {file_name}, please check the file path')
        exit(-1)