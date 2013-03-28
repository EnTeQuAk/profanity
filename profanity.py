# TODO items:
# leetspeak

profane_words = set()
with open('profane_words.txt') as f:
    for line in f.readlines():
        line = line.strip().lower()
        if line != '':
            profane_words.add(line.strip().lower())

dictionary_words = set()


def is_profane(text):
    # Check whole text for being profanity.
    if text in profane_words:
        return True

    # Check each word for being profanity.
    for word in text.lower().split():
        if word in profane_words:
            return True

    # Check substring profanity of length 5 or larger.
    for word in profane_words:
        if len(word) >= 5:
            if word in text:
                return True

    return False
