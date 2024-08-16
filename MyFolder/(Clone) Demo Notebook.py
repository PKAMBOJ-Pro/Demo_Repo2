# Databricks notebook source
print ("Hello World!!")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello world from my SQL!!"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC

# COMMAND ----------

# MAGIC %run ./Include/Full_name
# MAGIC
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)


# COMMAND ----------

display(files)
