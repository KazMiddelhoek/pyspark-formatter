from setuptools import setup, find_packages

setup(
    name="pyspark_formatter",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["pyspark-formatter=pyspark_formatter.main:run"]
    }
)