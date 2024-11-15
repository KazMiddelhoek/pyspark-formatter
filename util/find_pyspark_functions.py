import pyspark.sql.functions
from pyspark.sql import DataFrame
from inspect import getmembers, isfunction
import inspect


# get pyspark functions that take one or more columnOrName.
pyspark_functions = getmembers(pyspark.sql.functions, isfunction)
for func in pyspark_functions:
    sig = inspect.signature(func[1])
    if len(sig.parameters) == 1 and (
        ("col" in sig.parameters and sig.parameters["col"].annotation == "ColumnOrName")
        or (
            "cols" in sig.parameters
            and sig.parameters["cols"].annotation == "ColumnOrName"
        )
    ):
        print(func[0])
        # print(sig)

print("Now dataframe functions.")
# get dataframe functions that take one or more columnOrName.
dataframe_functions = getmembers(DataFrame, isfunction)
for func in dataframe_functions:
    sig = inspect.signature(func[1])
    if len(sig.parameters) == 2 and (
        ("col" in sig.parameters and sig.parameters["col"].annotation == "ColumnOrName")
        or (
            "cols" in sig.parameters
            and sig.parameters["cols"].annotation == "ColumnOrName"
        )
    ):
        print(func[0])
        # print(sig)
