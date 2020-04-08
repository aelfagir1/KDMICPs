import json
from stanfordcorenlp import StanfordCoreNLP
# Preset
host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port,timeout=30000)

#nlp=StanfordCoreNLP("http://localhost:9000/")
#s='Twenty percent electric motors are pulled from an assembly line'
s1='A young friend recently remarked that the worst boss he ever had would provide him with feedback that always consisted of You are doing a great job. But they both knew it was not true the organization was in disarray, turnover was excessive, and customers were not happy. My friend was giving it his all, but he needed more support and better feedback than he received. He wanted a leader who would be around when he needed them, and who would give him substantive advice, not platitudes. As a measure of his frustration, he said, I would rather have had a boss who yelled at me or made unrealistic demands than this one, who provided empty praise'
#s1 = open("C:/Users/aaeq8/Desktop/Spring 2020 Courses/KDM_Course/ICP2/textfile.txt")
#var = read.s1
output = nlp.annotate(s1, properties={"annotators":"tokenize,ssplit,pos,depparse,natlog,openie",
                                "outputFormat": "json",
                                 "openie.triple.strict":"true",
                                 "openie.max_entailments_per_clause":"20"})
a = json.loads(output)
print("The subject, object and verb/relation of the given sentence are")
print(a["sentences"][0]["openie"],'\n')
result = [a["sentences"][0]["openie"] for item in a]

for i in result:
    for rel in i:
        relationSent=rel['relation'],rel['subject'],rel['object']
        print('The triplet of the given sentence is')
        print(relationSent)


        def wordcount(args):
            pass


        def word_count(s1):
            counts = dict()
            words = s1.split()

            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

            return counts


        #print(word_count('the quick brown fox jumps over the lazy dog.'))
        print(word_count(s1))