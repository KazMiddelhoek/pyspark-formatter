from pyspark_formatter.col_in_select_formatter import ColInSelectTransformer
import libcst as cst


def test_col_in_select_formatter():
    module = cst.parse_module(
        """df.filter().select("a", f.col("b"), col("c"), col("d").alias("x"), pyspark.sql.functions.col("e"))"""
    )
    assert (
        module.visit(ColInSelectTransformer()).code
        == 'df.filter().select("a", "b", "c", col("d").alias("x"), "e")'
    )
