import libcst as cst
import libcst.matchers as m


class ColInSelectTransformer(cst.CSTTransformer):
    def leave_Call(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        if m.matches(updated_node.func, m.Attribute(attr=m.Name("select"))):
            for i, arg in enumerate(original_node.args):
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
