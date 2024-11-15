# pyspark-formatter
Automatically format your pyspark code based on best practices.

Under construction!

# Usage
To use this formatter, add it to your pre-commit-config:
```
  repos:
  - repo: https://github.com/KazMiddelhoek/pyspark-formatter
    rev: ... 
    hooks:
      - id: pyspark-formatter
```

# Implemented formatters
Currently, the following formatting rules are implemented:

## Unnecessary f.col() usage is removed.
```
import pyspark.sql.functions as f

df.select("a", f.col("b"), f.col("c").alias("d"))
```
becomes
```
df.select("a", "b", f.col("c").alias("d"))
```

## Unnecessary list usage in joins is removed.
```
df1.join(df2, ["join_column"], "inner")
```
becomes
```
df1.join(df2, "join_column", "inner")
```

