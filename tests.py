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
assassinscreed
shitake
shiitake
circumspection
sussex
cockburn
ashita
mauyamashita
ashitaka
fershita
yamashita
Aishiteru
amanashitra
"""
#WhoReallyCares

blacklist = """
cunt
shit
shitty
amotherfucker
badmotherfucker
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
fuckedyouup
fuckencio
fucker
fuckerfucker
fuckenshit
TheDick
thickdick
Trevor2dicks
Trickydick
Uncle_Nigga
youngniggacome
anuthanigga
bigassnigga
Nastybitch
niggabitch3217
FCUK-Hero
fcukme
fcukoyu
Buttholeyo
asspoop
gayaids
EvilPenis
homosapenis
LordPenis
noblepenis
penis33152
vaginaface
vaginabasher
Alottavagina
Massive Vagina
Mr.Pooper
Mr.Pooperskank
pooperino
sirturdboy
turdburglar
turdface
turdmuffin
unicornturd
wankerspanker
Wankoff
BigWanker
Asswhore
crack whore
darkwhore
"""
#bigfatdick
#TheBigDick
#thisgameisshit
#TurdFurguson
