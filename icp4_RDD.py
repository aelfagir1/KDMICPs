import pyspark
from pyspark.sql import SQLContext
from pyspark import SparkFiles
sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)

df = sqlContext.read.csv(SparkFiles.get("C:/Users/aaeq8/Desktop/Spring_2020_Courses/KDM_Course/ICP_4/data.csv"), header=True, inferSchema= True)
df.printSchema()


# show the rows with select and the names of the features
df.select('PhoneService','MultipleLines','PaymentMethod').show(7)

#To get a summary statistics
df.describe().show()