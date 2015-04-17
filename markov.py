import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make a string from them."""

        opened_text = []

        for filename in filenames:
            input_text = open(filename).read().strip("\n")
            opened_text.append(input_text)

        corpus = "".join(opened_text)

        return corpus


    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""

        chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)

            # or we could say "chains.setdefault(key, []).append(value)"

        return chains


    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(chains.keys())
        words = [key[0], key[1]]
        while key in chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)

            text = " ".join(words)

        return text

class AllLowercaseWordsMixin(object):
    """ Makes the markov text result all lowercase."""

    def make_lower(self, text):
        text = text.lower()

        return text

class TweetMarkov(SimpleMarkovGenerator,AllLowercaseWordsMixin):
    """Example subclass"""

if __name__ == "__main__":

    # Get a list of filenames from sys.argv
    filenames = sys.argv[1:]

    # # Make an instance of the class
    # markov_text_gen = SimpleMarkovGenerator()


    # # we should call the read_files method with the list of filenames
    # a = markov_text_gen.read_files(filenames)
    # b = markov_text_gen.make_chains(a)

    # # we should call the make_text method 5x
   
    # print markov_text_gen.make_text(b)
    # print

    # print markov_text_gen.make_text(b)
    # print 

    # print markov_text_gen.make_text(b)
    # print

    # print markov_text_gen.make_text(b)
    # print

    # print markov_text_gen.make_text(b)

    markov_text_lower = TweetMarkov()
    a = markov_text_lower.read_files(filenames)
    b = markov_text_lower.make_chains(a)
    c = markov_text_lower.make_text(b)
    print markov_text_lower.make_lower(c)