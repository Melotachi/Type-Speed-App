
import random
from app import TypeSpeed


def random_250_words():
    # Open the file
    words = []
    with open('most_common_1000_words.txt','r') as file:
        # Read the file
        words = file.readlines()
    
    word_list = []
    
    for i in range(250): # Choose 250 random words, you can change this number
        random_word = random.choice(words) # Choose a random word
        wanted_randem_word = random_word.strip('\n') # Remove the newline character
        word_list.append(wanted_randem_word)
        words.remove(random_word)  # Remove the word from the list so that it is not repeated
    
    return word_list


def main():
    
    words = random_250_words()

    my_app = TypeSpeed(words)



if __name__ == '__main__':
    
    main()







