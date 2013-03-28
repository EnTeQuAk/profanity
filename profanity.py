# TODO items:
# leetspeak

import re


def make_split_regex(word_list):
    def key(word):
        return -len(word), word
    word_list = list(word_list)
    word_list.sort(key=key)
    return re.compile(r'(%s)' % '|'.join(word_list))


profane_words = set()
egregious_words = set()
with open('profane_words.txt') as f:
    for line in f.readlines():
        word = line.strip().lower()
        if word == '':
            continue
        # Particularly bad profanity is marked with a star.
        if word.startswith('*'):
            word = word.lstrip('*')
            egregious_words.add(word)
        profane_words.add(word)
profane_regex = make_split_regex(profane_words)

dictionary_words = set()
common_words = set()
with open('dictionary_words.txt') as f:
    for line in f.readlines():
        word = line.strip().lower()
        if word == '':
            continue
        if word in profane_words:
            continue
        dictionary_words.add(word)
        # Also keep track of very common words for basic word
        # segmentation.
        if len(common_words) < 500 and len(word) >= 4:
            common_words.add(word)
common_words_regex = make_split_regex(common_words)


def is_profane(text):
    # Preprocessing.
    text = text.lower()
    text = re.sub(r'[^a-z]+', ' ', text)
    text = text.strip()

    # Check whole text for being profanity.
    if text in profane_words:
        return True

    # Check substring profanity for large or particularly egregious
    # profane words.
    for word in profane_words:
        if (
            len(word) >= 5 or
            word in egregious_words
        ):
            if word in text:
                return True

    # For shorter profane words, see if the context surrounding it
    # makes actual words.
    parts = profane_regex.split(text)
    parts = [p.strip() for p in parts if p != '']
    count = 0
    for p in parts:
        if len(p) < 3:
            continue
        if p in dictionary_words or p in profane_words:
            count += 1
    if count >= 2:
        return True

    return False


if __name__ == '__main__':
    import sys
    import os

    good = []
    bad = []

    filename = sys.argv[1]
    with open(filename) as f:
        seen = set()
        for line in f.readlines():
            line = line.strip()
            if line == '':
                continue
            if line in seen:
                continue
            seen.add(line)
            if is_profane(line):
                bad.append(line)
            else:
                good.append(line)

    with open(os.path.basename(filename) + '.good', 'w') as f:
        for line in good:
            f.write(line + '\n')

    with open(os.path.basename(filename) + '.bad', 'w') as f:
        for line in bad:
            f.write(line + '\n')
