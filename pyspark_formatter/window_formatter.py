import libcst as cst
import libcst.matchers as m

class PysparkWindowTransformer(cst.CSTTransformer):
    def __init__(self) -> None:
        pass

    def leave_Call(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        if m.matches(updated_node.func.value, m.Name(value="Window")) and m.matches(updated_node.func.attr, m.Name("partitionBy") | m.Name("orderBy")):
            for i, arg in enumerate(original_node.args):
                if isinstance(arg.value, cst.List):
                    args_with_unpacked_list = updated_node.args[:i]+tuple(cst.Arg(value=elem.value) for elem in arg.value.elements)+ updated_node.args[i+1:]
                    updated_node = updated_node.with_changes(args=args_with_unpacked_list)
        return updated_node