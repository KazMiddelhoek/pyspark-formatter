from pyspark_formatter.unnecessary_col_formatter import UncessecaryColTransformer
import libcst as cst


def test_unnecessary_col_formatter():
    module = cst.parse_module(
        """df.filter().select("a", f.col("b"), col("c"), col("d").alias("x"), pyspark.sql.functions.col("e"))"""
    )
    assert (
        module.visit(UncessecaryColTransformer()).code
        == 'df.filter().select("a", "b", "c", col("d").alias("x"), "e")'
    )
