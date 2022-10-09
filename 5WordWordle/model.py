from tkinter import W
import neat
from bktree import bkTree
from wordle import Wordle
from words import Words
import random
class Model():

    def run(self):
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
        # Load configuration.
        self.words = Words()
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation, r"config.config")

        # Create the population, which is the top-level object for a NEAT run.
        p = neat.Population(config)

        # Add a stdout reporter to show progress in the terminal.
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        p.add_reporter(neat.Checkpointer(5))

        # Run for up to 300 generations.
        winner = p.run(self.eval_genomes, 100)

        # Display the winning genome.
        # print('\nBest genome:\n{!s}'.format(winner))

        # Show output of the most fit genome against training data.
        # print('\nOutput:')
        winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
        # for xi, xo in zip(xor_inputs, xor_outputs):
        #     output = winner_net.activate(xi)
        #     print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))

        # node_names = {-1: 'A', -2: 'B', 0: 'A XOR B'}
        # visualize.draw_net(config, winner, True, node_names=node_names)
        # visualize.draw_net(config, winner, True, node_names=node_names, prune_unused=True)
        # visualize.plot_stats(stats, ylog=False, view=True)
        # visualize.plot_species(stats, view=True)

        # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
        # p.run(eval_genomes, 10)

    def eval_genomes(self, genomes, config):
        for genome_id, genome in genomes:
            genome.fitness = 0
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            data = [0] * 417
            notSolved = True
            totalGuesses = 0
            for k in range(50):
                wordle = Wordle(self.words.words, random)
                i = 0
                while (notSolved):
                    newData = wordle.guess(self.getWordFromOutput(net.activate(data)), data)
                    i += 1
                    if (len(newData) == 1 or i >= 100):
                        break
                    data = newData
                totalGuesses += i
            genome.fitness -= totalGuesses/50
            print(genome.fitness)


    def getWordFromOutput(self, output):
        bestWord = ""
        bestScore = -10000
        for k in range(len(self.words.words)):
            score = 0
            for z in range(5):
                score += output[self.alphabetMap.get(self.words.words[k][z])*5 + z]
            if score > bestScore:
                bestScore = score
                bestWord = self.words.words[k]
        return bestWord
                
