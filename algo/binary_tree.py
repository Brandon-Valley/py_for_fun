

class node:
    def __init__(self, value, right_node, left_node):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return f"{self.value=}, {self.left_node=}, {self.right_node=}"


def list_to_binary_tree(in_list) -> node:
    assert isinstance(in_list, list), type(in_list)

    if not in_list:
        return None
    
    def get_node_with_children_from_index(index) -> node:
        print(index)
        if index >= len(in_list):
            return None
        
        return node(
            value = in_list[index],
            left_node = get_node_with_children_from_index(2 * index + 1),
            right_node = get_node_with_children_from_index(2 * index + 2)
        )

    return get_node_with_children_from_index(0)



test_list = [1,2,3,4,5,6,7]

bt = list_to_binary_tree(test_list)
print(bt)