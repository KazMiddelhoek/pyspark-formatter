from pyspark_formatter.join_formatter import JoinTransformer
import libcst as cst


def test_join_formatter():
    module = cst.parse_module("""df1.join(df2, on=["a"], how="inner")
df1.join(df2)
df1.join(df2, ["a", "b"])
""")
    assert (
        module.visit(JoinTransformer()).code
        == """df1.join(df2, on="a", how="inner")
df1.join(df2)
df1.join(df2, ["a", "b"])
"""
    )
