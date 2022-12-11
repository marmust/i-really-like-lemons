def get_words(words):
    filepath = "i_rly_like_lemons/plug in words/" + words + ".txt"
    with open(filepath, "r") as file:
        return file.read()