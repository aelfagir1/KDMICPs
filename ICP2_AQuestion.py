from stanfordcorenlp import StanfordCoreNLP
# Preset
host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port,timeout=30000)

# The sentence you want to parse
sentence = ("The dog saw John in the park."
            "The little bear saw the fine fat trout in the rocky brook.")

# Tokenize
print('Tokenize：', nlp.word_tokenize(sentence))

# POS
print('POS：', nlp.pos_tag(sentence))

# NER
print('NER：', nlp.ner(sentence))

# Parser
print('Parser：')
print(nlp.parse(sentence))
print(nlp.dependency_parse(sentence))
# co-reference
print('Co-reference: ', nlp.coref(sentence))


# Close Stanford Parser
nlp.close()