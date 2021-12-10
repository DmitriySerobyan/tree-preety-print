class Tree:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


def pretty_print(tree, indent="", is_last=True):
    marker = "└──" if is_last else "├──"
    print(indent, marker, tree.value)
    indent += "   " if is_last else " │ "

    for index, child in enumerate(tree.children):
        pretty_print(child, indent, index == len(tree.children) - 1)


if __name__ == "__main__":
    tree = Tree(
        value="1",
        children=[
            Tree(
                value="1.1",
                children=[
                    Tree(value="1.1.1"),
                    Tree(value="1.1.2"),
                ]
            ),
            Tree(
                value="1.2",
                children=[
                    Tree(value="1.2.1"),
                    Tree(value="1.2.2"),
                    Tree(value="1.2.3"),
                ]
            )
        ]
    )

    pretty_print(tree)
