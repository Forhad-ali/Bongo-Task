class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


def lca(node1, node2):
    if node1.value == node2.value:
        print(node1.value)
        return

    node1_value = [node1.value]
    node2_value = [node2.value]

    while True:
        if node1.parent:
            node1 = node1.parent
            if node1.value in node2_values:
                print(node1.value)
                return
            node1_value.append(node1.value)

        if node2.parent:
            node2 = node2.parent
            if node2.value in node1_values:
                print(node2.value)
                return
            node2_value.append(node2.value)