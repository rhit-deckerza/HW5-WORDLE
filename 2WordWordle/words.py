


class Words():
    def __init__(self):
        my_file = open("LetterWords.txt", "r")
        # reading the file
        data = my_file.read()
        data_into_list = data.split("\n")
        self.words = []
        for k in range(len(data_into_list)):
            if (len(data_into_list[k]) == 2):
                self.words.append(data_into_list[k].lower())
        print(len(self.words))
        my_file.close()








