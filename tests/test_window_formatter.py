from pyspark_formatter.window_formatter import PysparkWindowTransformer
import libcst as cst


def test_window_formatter():
    module = cst.parse_module("""Window.partitionBy(["a", "b"]).orderBy("c")
pyspark.sql.Window().partitionBy("a").orderBy(["b", "c"])""")

    assert (
        module.visit(PysparkWindowTransformer()).code
        == """Window.partitionBy("a", "b").orderBy("c")
pyspark.sql.Window().partitionBy("a").orderBy("b", "c")"""
    )
