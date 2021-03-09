"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()
    


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    text_list = text_string.split()
    for i in range(len(text_list) - 2):
        word_tuple = (text_list[i], text_list[i+1])
        if word_tuple in chains:
            chains[word_tuple].append(text_list[i+2])
        else:
            chains[word_tuple] = [text_list[i+2]]
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    current_key = choice(list(chains.keys()))

    while True:
        words.append(current_key[0])
        if current_key not in chains:
            words.append(current_key[1])
            break
        current_key = (current_key[1], choice(chains[current_key]))
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
