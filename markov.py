"""Generate Markov text from text files."""

from random import choice
import sys 

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()
    
    

def make_chains(text_string, n):
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
    for i in range(len(text_list) - n):
        word_tuple = ()
        for j in range(n):
            word_tuple += (text_list[i + j],)
        if word_tuple in chains:
            chains[word_tuple].append(text_list[i+n])
        else:
            chains[word_tuple] = [text_list[i+n]]
    return chains


def make_text(chains, n):
    """Return text from chains."""

    words = []

    # your code goes here
    current_key = choice(list(chains.keys()))
    #current_key = ("For"", "a", "brief")
    #current_key[0] = "For"
    #current_key[0][0] = "F"
    while current_key[0][0].islower():
        current_key = choice(list(chains.keys()))

    while True:
        words.append(current_key[0])
        if current_key not in chains:
            words.extend(list(current_key[1:n]))
            break
        converted_tuple_list = list(current_key[1:n])
        converted_tuple_list.append(choice(chains[current_key]))
        current_key = tuple(converted_tuple_list)
    return ' '.join(words)

n = 4

input_path = str(sys.argv[1])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)
# Produce random text
random_text = make_text(chains, n)

print(random_text)
