

class Wordle():

    def __init__(self, words, random):
        ranIndex = random.randint(0, (len(words) - 1))
        self.goalWord = words[ranIndex]
        self.alphabetMap = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19,
            "u": 20,
            "v": 21,
            "w": 22,
            "x": 23,
            "y": 24,
            "z": 25
        }
    def guess(self, guess, data):
        answer = self.goalWord
        i = 0
        # if (answer == guess):
        #     return [1]
        # for letter in guess:
        #     if answer[i] == guess[i]: # Correct place
        #         x = (i+4) + 5*(self.alphabetMap.get(guess[i]))
        #         data[x] = 1
        #     elif letter in answer: # correct letter
        #         x = (2) + 5*(self.alphabetMap.get(guess[i]))
        #         data[x] = 1
        #         x = (3) + 5*(self.alphabetMap.get(guess[i]))
        #         data[x] = 1
        #     else: #not in word
        #         x = (1) + 5*(self.alphabetMap.get(guess[i]))
        #         data[x] = 1
        #     i += 1
        if (answer == guess):
            return [1]
        for letter in guess:
            if answer[i] == guess[i]: # Correct place
                if i == 0:
                    x = 1 + 2*(self.alphabetMap.get(guess[i]))
                    data[x] = 3
                else:
                    x = 2 + 2*(self.alphabetMap.get(guess[i]))
                    data[x] = 3
            elif letter in answer: # correct letter
                x = 1 + 2*(self.alphabetMap.get(guess[i]))
                data[x] = 2
                x = 2 + 2*(self.alphabetMap.get(guess[i]))
                data[x] = 2
            else: #not in word
                x = 1 + 2*(self.alphabetMap.get(guess[i]))
                data[x] = 0
                x = 2 + 2*(self.alphabetMap.get(guess[i]))
                data[x] = 0
            i += 1
        # z = 0
        # for k in self.alphabetMap:
        #     print(k + ":")
        #     string = ""
        #     for x in range (5):
        #         string += str(data[1 +x + 5*z])
        #     print(string)
        #     z += 1
        data[0] += 1
        return data