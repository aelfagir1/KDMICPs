import pyspark
from pyspark.sql import SQLContext
from pyspark import SparkFiles
sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)

df = sqlContext.read.csv(SparkFiles.get("C:/Users/aaeq8/Desktop/Spring_2020_Courses/KDM_Course/ICP_4/data.csv"), header=True, inferSchema= True)

#rename column
newdf = {
    'Churn':'Chureeen',
    'TotalCharges': 'allfees'

}
df(columns=newdf, inpleace=True)
df.sort(by=['SeniorCitizen'], inplace=True)

df.printSchema()
#sortdata by SeniorCitizen
