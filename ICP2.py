#import nltk
from stanfordcorenlp import StanfordCoreNLP
# Preset
host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port,timeout=30000)
# The sentence you want to parse
f = open("C:/Users/aaeq8/Desktop/Spring 2020 Courses/KDM_Course/ICP2/textfile.txt", "r")
for x in f:
    sentence = x
    print("Cureent sentence is : ", sentence )
    # Tokenize
    print('Tokenize for this sentence：', nlp.word_tokenize(sentence))
    # POS
    print('POS for this sentence：', nlp.pos_tag(sentence))
    # NER
    print('NER for this sentence：', nlp.ner(sentence))
    # Parser
    print('Parser for this sentence：')
    print(nlp.parse(sentence))
    print(nlp.dependency_parse(sentence))
    # co-reference
    print('Co-reference for this sentence: ', nlp.coref(sentence))
# Close Stanford Parser
nlp.close()
f.close()