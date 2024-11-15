# pyspark-formatter
Automatically format your pyspark code based on best practices. Generally, this comes down to keeping your code as simple 
as possible by removing redundant function calls, list creation etc. Some rules are inspired by the [palantir style guide](https://github.com/palantir/pyspark-style-guide). This repo does currently does not use type checking to determine what to clean up, and may
therefore have some false positives. Feel free to report them!

Under construction!

# Usage
To use this formatter, add it to your pre-commit-config:
```
  repos:
  - repo: https://github.com/KazMiddelhoek/pyspark-formatter
    rev: v0.0.1 
    hooks:
      - id: pyspark-formatter
```

# Implemented formatters
Currently, the following formatting rules are implemented:

### Unnecessary f.col() calls are removed.
```
import pyspark.sql.functions as f

df.select("a", f.col("b"), f.col("c").alias("d"))
df.withColumn("a", f.cos(f.col("b")))
```
becomes
```
df.select("a", "b", f.col("c").alias("d"))
df.withColumn("a", f.cos("b"))
```

### Unnecessary lists in joins and windows are removed.
```
df1.join(df2, ["join_column"], "inner")
w = Window.partitionBy(["a", "b"]).orderBy(["c"])
```
becomes
```
df1.join(df2, "join_column", "inner")
w = Window.partitionBy("a", "b").orderBy("c")
```
