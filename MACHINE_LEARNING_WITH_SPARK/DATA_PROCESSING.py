#!/usr/bin/env python
# coding: utf-8

# # EVOLUTION OF DATA
# 
# Hernan Carlos Chavez Paura Garcia<br>
# Feb 8th, 2025<br>
# Singh, Pramod. Machine Learning with PySpark: With Natural Language Processing and Recommender Systems. Apress, 2018.

# ## LOAD AND RELOAD DATA

# In[1]:


# pip install pyspark


# In[2]:


# We start with importing and creating the SparkSession object first in order to use Spark.
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('data_procesing').getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
df = spark.read.csv('MACHINE_LEARNING_WITH_SPARK_MATERIAL/machine-learning-with-pyspark-master/chapter_2_Data_Processing/sample_data.csv', 
                    inferSchema=True, header=True)


# In[3]:


df.columns


# In[4]:


len(df.columns)


# In[5]:


df.count()


# In[6]:


print((df.count()),(len(df.columns)))


# In[7]:


df.printSchema()


# In[8]:


df.show(3)


# In[9]:


df.select('age', 'mobile').show(5)


# In[10]:


df.describe().show()


# ## ADDING A NEW COLUMN

# In[11]:


df.withColumn('age_after_10_years',(df['age'] + 10)).show(10,False)


# In[12]:


df.show()


# In[13]:


df_test = df.withColumn('age_after_10_years',(df['age'] + 10))
df_test.show()


# In[14]:


from pyspark.sql.types import StringType, DoubleType
df.withColumn('age_double', df['age'].cast(DoubleType())).show(10,False)


# ## FILTERING DATA

# In[15]:


df.filter(df['mobile'] == 'Vivo').show()


# In[16]:


df.filter(df['mobile'] == 'Vivo').select('age','ratings','mobile').show()


# In[17]:


df.filter(df['mobile'] == 'Vivo').filter(df['experience'] > 10).show()


# In[18]:


df.filter((df['mobile'] == 'Vivo')&(df['experience'] > 10)).show()


# ## DISTINCT VALUES IN COLUMN

# In[19]:


df.select('mobile').distinct().show()


# In[20]:


df.select('mobile').distinct().count()


# ## GROUPING DATA

# In[21]:


df.groupBy('mobile').count().show(5,False)


# In[22]:


df.groupBy('mobile').count().orderBy('count', ascending = False).show(5, False)


# In[23]:


df.groupBy('mobile').mean().show(5,False)


# In[24]:


df.groupBy('mobile').sum().show(5,False)


# In[25]:


df.groupBy('mobile').max().show(5,False)


# In[26]:


df.groupBy('mobile').min().show(5,False)


# ## AGGREGATIONS

# In[27]:


df.groupBy('mobile').agg({'experience': 'sum'}).show(5,False)


# ## USER-DEFINED FUNCTIONS (UDF's)
# 
# * Conventional UDF
# * Pandas UDF
# 
# Pandas UDF are much more powerful in terms of speed and processing time.

# In[28]:


from pyspark.sql.functions import udf


# ## CONVENTIONAL UDF: USING TRADITIONAL PYTHON FUNCTION

# In[29]:


def price_range(brand):
    if brand in ['Smasung','Apple']:
        return'High Price'
    elif brand == 'MI':
        return 'Mid Price'
    else:
        return 'Low Price'
    
brand_udf = udf(price_range,StringType())


# In[30]:


df.withColumn('price_range',brand_udf(df['mobile'])).show(10,False)


# ## CONVENTIONAL UDF: USING LAMBDA FUNCTION

# In[31]:


age_udf = udf(lambda age: "young" if age <= 30 else "senior", StringType())
df.withColumn("age_group", age_udf(df.age)).show(10,False)


# ## PANDAS UDF (VECTORIZED UDF)
# 
# There are two types of Pandas UDFs:
# 
# * Scalar
# * GroupedMap

# In[32]:


from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import IntegerType

def remaining_yrs(age):
    yrs_left = (100 - age)
    return yrs_left

length_udf = pandas_udf(remaining_yrs, IntegerType())
df.withColumn("yrs_left", length_udf(df['age'])).show(10,False)


# ## PANDAS UDF (MULTIPLE COLUMNS)

# In[33]:


def prod(rating,exp):
    x = rating * exp
    return x

prod_udf = pandas_udf(prod, DoubleType())

df.withColumn("product", prod_udf(df['ratings'],df['experience'])).show(10,False)


# ## DROP DUPLICATE VALUES

# In[34]:


df.count()


# In[35]:


df = df.dropDuplicates()
df.count()


# ## DELETE COLUMN

# In[36]:


df_new = df.drop('mobile')
df_new.show()


# ## WRITTING DATA: CSV

# In[37]:


pwd


# In[38]:


write_uri = '/Users/c105624/Desktop/JUPYTER_NOTEBOOK/df_csv'
df.coalesce(1).write.format("csv").option("header", True).save(write_uri)


# ## WRITTING DATA: PARQUET

# In[39]:


parquet_uri = '/Users/c105624/Desktop/JUPYTER_NOTEBOOK/df_parquet'
df.coalesce(1).write.format('parquet').save(parquet_uri)

