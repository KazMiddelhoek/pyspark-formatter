import libcst as cst
import libcst.matchers as m


class UncessecaryColTransformer(cst.CSTTransformer):
    def __init__(self) -> None:
        self.pyspark_functions_that_take_strings = {
            "abs",
            "acos",
            "acosh",
            "array_distinct",
            "array_max",
            "array_min",
            "array_sort",
            "arrays_zip",
            "asc",
            "asc_nulls_first",
            "asc_nulls_last",
            "ascii",
            "asin",
            "asinh",
            "atan",
            "atanh",
            "avg",
            "base64",
            "bin",
            "bit_length",
            "bitwiseNOT",
            "bitwise_not",
            "cbrt",
            "ceil",
            "coalesce",
            "collect_list",
            "collect_set",
            "concat",
            "cos",
            "cosh",
            "cot",
            "count",
            "crc32",
            "csc",
            "dayofmonth",
            "dayofweek",
            "dayofyear",
            "days",
            "degrees",
            "desc",
            "desc_nulls_first",
            "desc_nulls_last",
            "exp",
            "explode",
            "explode_outer",
            "expm1",
            "factorial",
            "flatten",
            "floor",
            "greatest",
            "grouping",
            "grouping_id",
            "hash",
            "hex",
            "hour",
            "hours",
            "initcap",
            "isnan",
            "isnull",
            "kurtosis",
            "least",
            "length",
            "log10",
            "log1p",
            "log2",
            "lower",
            "ltrim",
            "map_entries",
            "map_from_entries",
            "map_keys",
            "map_values",
            "max",
            "md5",
            "mean",
            "min",
            "minute",
            "month",
            "months",
            "octet_length",
            "posexplode",
            "posexplode_outer",
            "product",
            "quarter",
            "radians",
            "reverse",
            "rint",
            "rtrim",
            "sec",
            "second",
            "sha1",
            "shuffle",
            "signum",
            "sin",
            "sinh",
            "size",
            "skewness",
            "soundex",
            "sqrt",
            "stddev",
            "stddev_pop",
            "stddev_samp",
            "sum",
            "sumDistinct",
            "sum_distinct",
            "tan",
            "tanh",
            "timestamp_seconds",
            "toDegrees",
            "toRadians",
            "trim",
            "unbase64",
            "unhex",
            "upper",
            "var_pop",
            "var_samp",
            "variance",
            "weekofyear",
            "xxhash64",
            "year",
            "years",
        }
        self.dataframe_functions_that_take_strings = {
            "_jcols",
            "cube",
            "drop",
            "groupBy",
            "rollup",
            "select",
            "toDF",
        }

    def leave_Call(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        if m.matches(
            updated_node.func,
            m.Attribute(
                attr=m.OneOf(*[
                    m.Name(func)
                    for func in self.dataframe_functions_that_take_strings.union(self.pyspark_functions_that_take_strings)
                ]
                )
            ),
        ) or m.matches(
            updated_node.func,
            m.OneOf(m.Name(func) for func in self.pyspark_functions_that_take_strings),
        ):
            for i, arg in enumerate(updated_node.args):
                if m.matches(
                    arg.value,
                    m.Call(func=m.Attribute(attr=m.Name("col")))
                    | m.Call(func=m.Name("col")),
                ):
                    args_with_unpacked_list = (
                        updated_node.args[:i]
                        + (
                            cst.Arg(
                                value=arg.value.args[0].value,
                                comma=arg.comma,
                                whitespace_after_arg=arg.whitespace_after_arg,
                            ),
                        )
                        + updated_node.args[i + 1 :]
                    )
                    updated_node = updated_node.with_changes(
                        args=args_with_unpacked_list
                    )
        return updated_node
