import libcst as cst
import libcst.matchers as m


class JoinTransformer(cst.CSTTransformer):
    def leave_Call(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        if m.matches(
            updated_node,
            m.Call(
                func=m.Attribute(attr=m.Name(value="join")),
                args=[
                    m.DoNotCare(),
                    m.Arg(value=m.List(elements=[m.DoNotCare()])),
                    m.ZeroOrMore(),
                ],
            ),
        ):
            list_arg = updated_node.args[1]
            list_arg = list_arg.with_changes(value=list_arg.value.elements[0].value)
            updated_node = updated_node.with_changes(
                args=updated_node.args[:1] + (list_arg,) + original_node.args[2:]
            )

        # TODO's
        # format 'on' argument:
        # if list with f.col (no equalities etc.), replace with string names.

        return updated_node
