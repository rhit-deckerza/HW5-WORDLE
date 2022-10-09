


class Words():
    def __init__(self):
        my_file = open("5LetterWords.txt", "r")
        # reading the file
        data = my_file.read()
        data_into_list = data.split("\n")
        self.words = data_into_list
        print(len(data_into_list))
        my_file.close()








