#  __                                      __  __                  __  __  __                        __                                                       
# |  \                                    |  \|  \                |  \|  \|  \                      |  \                                                      
#  \$$        ______    ______    ______  | $$| $$ __    __       | $$ \$$| $$   __   ______        | $$  ______   ______ ____    ______   _______    _______ 
# |  \       /      \  /      \  |      \ | $$| $$|  \  |  \      | $$|  \| $$  /  \ /      \       | $$ /      \ |      \    \  /      \ |       \  /       \
# | $$      |  $$$$$$\|  $$$$$$\  \$$$$$$\| $$| $$| $$  | $$      | $$| $$| $$_/  $$|  $$$$$$\      | $$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\| $$$$$$$\|  $$$$$$$
# | $$      | $$   \$$| $$    $$ /      $$| $$| $$| $$  | $$      | $$| $$| $$   $$ | $$    $$      | $$| $$    $$| $$ | $$ | $$| $$  | $$| $$  | $$ \$$    \ 
# | $$      | $$      | $$$$$$$$|  $$$$$$$| $$| $$| $$__/ $$      | $$| $$| $$$$$$\ | $$$$$$$$      | $$| $$$$$$$$| $$ | $$ | $$| $$__/ $$| $$  | $$ _\$$$$$$\
# | $$      | $$       \$$     \ \$$    $$| $$| $$ \$$    $$      | $$| $$| $$  \$$\ \$$     \      | $$ \$$     \| $$ | $$ | $$ \$$    $$| $$  | $$|       $$
#  \$$       \$$        \$$$$$$$  \$$$$$$$ \$$ \$$ _\$$$$$$$       \$$ \$$ \$$   \$$  \$$$$$$$       \$$  \$$$$$$$ \$$  \$$  \$$  \$$$$$$  \$$   \$$ \$$$$$$$ 
#                                                 |  \__| $$                                                                                                  
#                                                  \$$    $$                                                                                                  
#                                                   \$$$$$$                                                                                                   
#
#
#       - source code
#       - made by 8AAFFF
#       - extras submodule

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# import get_words
import get_words

# clean a text up from all unwanted characters
def cleanup(text):
    # define the variable we will be copying the clean text into
    clean = ""
    
    # loop over every single character of the text we are cleaning up
    for x in range(len(text)):
        # if the character is not dirty (not inside the filter from get_words)
        if text[x] not in get_words.get_words("filter"):
            # we add it to the clean characters
            clean += text[x]
        else:
            # if its dirty, then we just skip it and go to the next character
            pass
    
    return clean

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# split a string into a list with multiple seperatos
# when running function dont forget to declate variables like so:
# split_with_multiple_seperators(",", ".", " ", "|", text = "sep1, sep2. sep3 sep4| some more text")
def split_with_multiple_seperators(*seperators, text):
    # put all the seperators into a string like so:
    # [",", ".", "/"]   -->   ",./"
    seperators = "".join(list(seperators))
    # define the copied var which we will be pasting into all the not seperatror text
    copied = ""
    # define final list in which we will be appending all the seperated text
    final = []

    # loop over each character in the text
    for x in range(len(text)):
        # if the character that we are looking at is NOT a seperator, we add it to copied
        if text[x] not in seperators:
            copied = copied + text[x]
        # if the character IS a seperator, then we append copied to final, and reset copied to = ""
        else:
            final.append(copied)
            copied = ""

    # append whatever is left in copied to final and return final
    final.append(copied)

    return final

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# a function to lightly rephrase a sentence
def rephrase(indexes, strength):
    import random
    
    # loop over the indexes list
    for x in range(len(indexes)):
        # change every index to a itself + a random number
        indexes[x] = indexes[x] + random.randint(-strength, strength)
        
    return indexes

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# get the match precentage of 2 strings
# test and twst > 75.0% match
def compare(word1, word2):
    # define shorter and longer
    shorter = ""
    longer = ""
    # define "match" witch we will later be adding the amount of similar letters
    match = 0
    
    # set shorter as the shorter word, and longer as the longer word
    # if they are the same: shorter = word1, longer = word2
    # we do this since we want to compare the shorter word to the longer word and not the other way around because:
    # we cant compare the: for example: the 5th letter of a 6 letter word, to the 5th letter of a 4 letter word
    if len(word1) > len(word2):
        shorter = word2
        longer = word1
    elif len(word1) < len(word2):
        shorter = word1
        longer = word2
    else:
        shorter = word1
        longer = word2
    
    # loop over the shorter word
    for x in range(len(shorter)):
        # add the amount of the letter[x] of shorter word in the longer word to match
        match += longer.count(shorter[x])
    
    # return match / length of longer
    # devide by len(longer) because we want to get a relative value that is not affected by the word's length
    return match / len(longer)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# a function to autocorrect a signel word
# it works by looping over all words and returning the closest match (using compare func)
def autocorrect_word(word, library):
    # define the closest (text) and the closest (index) of the list we are comparing to
    closest = ""
    closest_match = 0
    
    # loop over the full autocorrect library that is given to the function
    for x in range(len(library)):
        # check if the word is the closest we found yet
        if compare(word, library[x]) >= closest_match:
            # if IT IS the closest, set it as the closest (txet) and closest (index)
            closest_match = compare(word, library[x])
            closest = library[x]
        else:
            pass
    
    # return it
    return closest

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# autocorrect a full sentence / text
def autocorrect_text(text):
    # clean up the text from unwanted characters, and turn in into a list (on every space)
    text = cleanup(text).split()
    # get the words that we want to be checking (autocorrecting tto)
    library = get_words.get_words("everything").split("\n")
    # define the list that we will be appending the corrected words to.
    corrected = []
    
    # loop over every word in the incorrect text
    for x in range(len(text)):
        # addd the corrected word to the list
        corrected.append(autocorrect_word(text[x], library))
    
    # return the corrected list (we join it back into a string with space " ")
    return " ".join(corrected)