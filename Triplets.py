import json
from stanfordcorenlp import StanfordCoreNLP


# Preset
host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port,timeout=30000)

#nlp=StanfordCoreNLP("http://localhost:9000/")
#s='Twenty percent electric motors are pulled from an assembly line'
s1='Introduction, The field of Health Informatics is on the cusp of its most exciting period to date, entering a new era where technology is starting to handle Big Data, bringing about unlimited potential for information growth. Data mining and Big Data analytics are helping to realize the goals of diagnosing, treating, helping, and healing all patients in need of healthcare, with the end goal of this domain being improved Health Care Output (HCO), or the quality of care that healthcare can provide to end users (i.e. patients). Health Informatics is a combination of information science and computer science within the realm of healthcare. There are numerous current areas of research within the field of Health Informatics, including Bioinformatics, Image Informatics (e.g. Neuroinformatics), Clinical Informatics, Public Health Informatics, and also Translational BioInformatics (TBI).'
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