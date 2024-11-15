# import libcst as cst
# from libcst.metadata import ParentNodeProvider


# class PysparkWindowTransformer(cst.CSTTransformer):
#     METADATA_DEPENDENCIES = (ParentNodeProvider,)

#     # def leave_Call(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
#     #     print(dump(updated_node))
#     #     if (m.matches(updated_node.func.value, m.Name(value="Window"))
#     #        # m.matches(updated_node.func.value.func.value, m.Name(value="Window"))
#     #     )  and m.matches(updated_node.func.attr, m.Name("partitionBy") | m.Name("orderBy")):
#     #         for i, arg in enumerate(original_node.args):
#     #             if isinstance(arg.value, cst.List):
#     #                 #args_with_unpacked_list = updated_node.args[:i]+tuple(cst.Arg(value=elem.value) for elem in arg.value.elements)+ updated_node.args[i+1:]
#     #                 updated_node = updated_node.with_deep_changes(updated_node.args[i], value=cst.FlattenSentinel(tuple(cst.Arg(value=elem.value) for elem in arg.value.elements)))
#     #     return updated_node

#     def leave_Arg(self, original_node: cst.List, updated_node: cst.List) -> cst.List:
#         if isinstance(updated_node.value, cst.List):
#             # test =self.get_metadata(ParentNodeProvider, original_node)
#             return cst.FlattenSentinel(
#                 tuple(cst.Arg(value=elem.value) for elem in updated_node.value.elements)
#             )
#         return updated_node#
