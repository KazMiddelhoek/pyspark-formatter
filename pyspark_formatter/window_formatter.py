import libcst as cst
import libcst.helpers
import libcst.matchers as m


class PysparkWindowTransformer(cst.CSTTransformer):
    def leave_Call(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        if m.matches(
            updated_node,
            m.Call(
                func=m.Attribute(
                    attr=m.Name(value="partitionBy") | m.Name(value="orderBy")
                ),
                args=(m.Arg(value=m.List()),),
            ),
        ) and "Window." in libcst.helpers.get_full_name_for_node(updated_node):
            updated_node = updated_node.with_changes(
                args=tuple(
                    cst.Arg(value=elem.value)
                    for elem in updated_node.args[0].value.elements
                )
            )
        return updated_node
