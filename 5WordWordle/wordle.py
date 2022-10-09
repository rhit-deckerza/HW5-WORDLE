

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

    def correct_place(self, letter):
        return "2"


    def correct_letter(self, letter):
        return "1"


    def incorrect_letter(self, letter):
        return "0"

    
    def guess(self, guess, data):
        answer = self.goalWord
        print(answer)
        i = 0
        if (answer == guess):
            return [1]
        for letter in guess:
            if answer[i] == guess[i]: # Correct place
                x = (i+11) + 15*(self.alphabetMap.get(guess[i]))
                data[x] = 1
            elif letter in answer: # correct letter
                x = (6) + 15*(self.alphabetMap.get(guess[i]))
                data[x] = 1
                x = (7) + 15*(self.alphabetMap.get(guess[i]))
                data[x] = 1
                x = (8) + 15*(self.alphabetMap.get(guess[i]))
                data[x] = 1
                x = (9) + 15*(self.alphabetMap.get(guess[i]))
                data[x] = 1
                x = (10) + 15*(self.alphabetMap.get(guess[i]))
                data[x] = 1
            else: #not in word
                x = (1) + 15*(self.alphabetMap.get(guess[i]))
                data[x] = 1
                x = (2) + 15*(self.alphabetMap.get(guess[i]))
                data[x] = 1
                x = (3) + 15*(self.alphabetMap.get(guess[i]))
                data[x] = 1
                x = (4) + 15*(self.alphabetMap.get(guess[i]))
                data[x] = 1
                x = (5) + 15*(self.alphabetMap.get(guess[i]))
                data[x] = 1
            i += 1
        z = 0
        for k in self.alphabetMap:
            print(k + ":")
            string = ""
            for x in range (15):
                string += str(data[1 +x + 15*z])
                # print(z*x)
            print(string)
            z += 1
        data[0] += 1
        return data