from pyspark import SparkContext
sc = SparkContext("spark://spark-master:7077", "PopularItems")
data = sc.textFile("/tmp/data/access.log", 2)
pairs = data.map(lambda line: line.split("\t"))

pages = pairs.map(lambda pair: (pair[1], 1))
count = pages.reduceByKey(lambda x,y: x+y)

output = count.collect()
for page_id, count in output:
    print("page_id %s count %d" % (page_id, count))
print ("Popular items done")

sc.stop()
