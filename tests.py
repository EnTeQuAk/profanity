from nose.tools import assert_true, assert_false

from profanity import is_profane


def test_whitelist():
    def check(word):
        assert_false(is_profane(word), word)
    for word in process_words(whitelist):
        yield check, word


def test_blacklist():
    def check(word):
        assert_true(is_profane(word), word)
    for word in process_words(blacklist):
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
circumspection
sussex
cockburn
ashita
mauyamashita
"""

blacklist = """
cunt
shit
shitty
amotherfucker
badmotherfucker
shitsonstuff
BadMothaFuckef
BADMUTHAFUCKA
BigFuckOffSpel
henchfucktard
hornyfuck
cumbucket
nigger123
niggeratti
niggerbang
Niggerbicth
niggerdick
niggerfagbag
niggerfaggot69
niggerjoe
niggerkiller
Niggerloo
niggermang
niggershit
niggerslave
niggersmell
niggerss
niggertits
dr.Faggot
totoasshole
eatthepoopoo
eatshit2
shiteater2
"""
