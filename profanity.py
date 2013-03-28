# TODO items:
# leetspeak

import re

profane_words = set()
with open('profane_words.txt') as f:
    for line in f.readlines():
        line = line.strip().lower()
        if line == '':
            continue
        profane_words.add(line)
profane_regex = '|'.join(profane_words)

dictionary_words = set()
with open('common_words.txt') as f:
    for line in f.readlines():
        line = line.strip().lower()
        if line == '':
            continue
        if line in profane_words:
            continue
        dictionary_words.add(line)


def is_profane(text):
    # Preprocessing.
    text = text.lower()
    text = re.sub(r'[^a-z]+', ' ', text)
    print(text)
    text = text.strip()

    # Check whole text for being profanity.
    if text in profane_words:
        return True

    # Check substring profanity.
    for word in profane_words:
        if len(word) >= 5 or word == 'fuck':
            if word in text:
                return True

    # For shorter profane words, see if the context surrounding it
    # makes actual words.
    parts = re.split(
        '(%s)' % profane_regex,
        text,
    )
    parts = [p for p in parts if p != '']
    count = 0
    for p in parts:
        if p in dictionary_words or p in profane_words:
            count += 1
    if count >= 2:
        return True

    return False


if __name__ == '__main__':
    import sys
    for line in sys.stdin.readlines():
        line = line.strip()
        if not is_profane(line):
            print(line)
