

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

# step 2
def print_flattened_values(node):
    def _print_min(node):
        if not node:
            return
        
        _print_min(node.left_node)
        print(node.value, end=", ")
        _print_min(node.right_node)

    _print_min(node)


# step 4
def get_in_order_for_level(bt_root, level):
    assert isinstance(bt_root, node)
    assert isinstance(level, int)
    assert level >= 0

    def _get_result_list(cur_node = bt_root, cur_level = 0, result_list = None):
        if not result_list:
            result_list = []

        if cur_level == level:
            # print(cur_node.value, end=" ")
            result_list.append(cur_node.value)
            return result_list
        
        if cur_node.left_node:
            result_list.extend(_get_result_list(cur_node.left_node, cur_level + 1))
        if cur_node.right_node:
            result_list.extend(_get_result_list(cur_node.right_node, cur_level + 1))

        return result_list

    return _get_result_list()





test_list = [1,2,3,4,5,6,7]

bt_root = list_to_binary_tree(test_list)
print(bt_root)

# step 2
print(f"{print_flattened_values(bt_root)=}")


print("\nSTEP 3 get_in_order_for_level()")
print(f"{get_in_order_for_level(bt_root,0)=}")
print(f"{get_in_order_for_level(bt_root,1)=}")
print(f"{get_in_order_for_level(bt_root,2)=}")
print(f"{get_in_order_for_level(bt_root,3)=}")
