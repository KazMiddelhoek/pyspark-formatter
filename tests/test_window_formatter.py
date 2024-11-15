from pyspark_formatter.window_formatter import PysparkWindowTransformer
import libcst as cst
from libcst.metadata import MetadataWrapper


def test_window_formatter():
    module = cst.parse_module("""Window.partitionBy(["a", "b"]).orderBy(["c"], "d")                    
                              """)
    wrapper = MetadataWrapper(module)
    print(wrapper)
    assert (
        wrapper.visit(PysparkWindowTransformer()).code
        == 'Window.partitionBy("a", "b").orderBy("c", "d")'
    )
