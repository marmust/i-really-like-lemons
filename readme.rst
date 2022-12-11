how to use:

sentiment analysis:

    from i_rly_like_lemons import sentiment

    1: get_sentence_sentiment("your sentence here")   <--   returns a single number which is the sentence's sentiment.

    2: get_text_sentiment("i really like lemons, however pineapples are also good. and this is another sentence.")   <---   returns a list of all sentiments from the sentences.

meaning extraction:

    from i_rly_like_lemons import meaning

    1: word_to_index("word")   <---   returns the "meaning index" of a single word.

    2: index_to_word(912873)   <---   gets the "meaning index" of a word, and translates the index into the word.

    3: sentence_to_index("your sentence here")   <---   gets a sentence and returns the list of all meaning indexe's of the words inside.

    4: index_to_sentence([129038, 238745, 39874,... 93824])   <---   gets a list of meaning indexe's and returns a sentence.

keyword detection:

    from i_rly_like_lemons import keywords

    1: detect_keywords("your sentence here")   <---   will get a text prompt and return a list with all the keywords that it found.

extras:

    from i_rly_like_lemons import extras

    1: cleanup("you,r co<<rupte///d [tex]t he.re")   <---   will get text and clean it up from unwanted characters (all special characters).

    2: split_with_multiple_seperators("|", ",", " ", text = "this|is,a test")   <--- just like normal split(" ") command but supports multiple seperators.

    3: rephrase([238094, 78245, 879435, 38490], 2)   <--- takes in a meaning list (from meaning extraction) and randomizes them with the "strength" value.

    4: compare("word1", "werd2")   <--- gets two strings and returns the % of their match: 0% > no matching characters, 100% > identical strings.

    5: autocorrect_word("misspled")   <--- gets a word and autocorrects it
    
    6: autocorrect_text("ths si a misppled txte")   <--- gets a wrond text and autocorrects it