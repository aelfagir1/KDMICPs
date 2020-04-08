# importing the library
from nltk.corpus import wordnet

# lets use word paint as an exqmple
syns = wordnet.synsets('excellent')
# An example of a synset:
print(syns[0].name())
print('\n')

print(syns[0].examples())
print('\n')


# lets use word paint as an exqmple
syns = wordnet.synset('excellent.s.01') .part_hyponyms('excellent.s.01')
# An example of a synset:
print(hyponyms[0].name())

# synonyms and antonyms using wordnet using word
holonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.holonyms():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print('The synonyms of good are: ')
print(set(synonyms))
print('\n')
print('The antonyms of good are: ')
print(set(antonyms))
print('\n')
rint('\n')