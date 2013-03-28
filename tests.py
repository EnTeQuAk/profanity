from nose.tools import assert_true, assert_false

from profanity import is_profane


def test_whitelist():
    def check(word):
        assert_false(is_profane(word), word)
    for word in whitelist:
        yield check, word


def test_blacklist():
    def check(word):
        assert_true(is_profane(word), word)
    for word in blacklist:
        yield check, word


def process_words(words_text):
    return [
        word.strip() for word in
        words_text.lower().split('\n')
        if len(word.strip()) > 0
    ]


whitelist = """
scunthorpe
assassin
shitake
shiitake
"""
whitelist = process_words(whitelist)

blacklist = """
cunt
shit
shitty
amotherfucker
badmotherfucker
BadMothaFuckef
"""
blacklist = process_words(blacklist)
