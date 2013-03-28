bad_words = set()
with open('badwords.txt') as f:
    for line in f.readlines():
        line = line.strip().lower()
        if line != '':
            bad_words.add(line.strip().lower())


def is_profane(text):
    print(text.lower().split())
    print(bad_words)
    for word in text.lower().split():
        if word in bad_words:
            return True
    return False
