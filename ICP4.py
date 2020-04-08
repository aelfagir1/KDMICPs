import pyspark
if not 'sc' in globals():
    sc = pyspark.SparkContext()
text_file = sc.textFile("C:/Users/aaeq8/Desktop/Spring_2020_Courses/KDM_Course/ICP_4/example.txt")
#System.setProperty("hadoop.home.dir","C:\Hadoop\bin\winutils.exe")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
for x in counts.collect():
    print (x)

