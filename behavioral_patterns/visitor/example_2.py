"""
 Consider a simple expression tree, and we want to implement a visitor that evaluates the tree and returns the result of the expression.
 """

 class Node:
    def accept(self, visitor):
        pass

class NumberNode(Node):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_number(self)

class AddNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_add(self)

class MultiplyNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_multiply(self)

class Evaluator(NodeVisitor):
    def visit_number(self, node):
        return node.value

    def visit_add(self, node):
        return node.left.accept(self) + node.right.accept(self)

    def visit_multiply(self, node):
        return node.left.accept(self) * node.right.accept(self)


def main():
    # expression tree
    #  *
    # / \
    #2   +
    #   / \
    #  3   4

    tree = MultiplyNode(
        NumberNode(2),
        AddNode(
            NumberNode(3),
            NumberNode(4)
        )
    )

    evaluator = Evaluator()
    print(tree.accept(evaluator)) # 14


if __name__ == '__main__':
    main()
