

from collections import deque


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


# step 3
def get_in_order_for_level(bt_root, level):
    assert isinstance(bt_root, node)
    assert isinstance(level, int)
    assert level >= 0

    result = []

    def _inner(cur_node = bt_root, cur_lvl = 0):
        nonlocal result

        if cur_lvl == level:
            result.append(cur_node.value)
            return

        if cur_node.left_node:
            _inner(cur_node.left_node, cur_lvl + 1)
        if cur_node.right_node:
            _inner(cur_node.right_node, cur_lvl + 1)

    _inner()
    return result


# step 4 - inspired by https://leetcode.com/problems/populating-next-right-pointers-in-each-node/solutions/1654181/c-python-java-simple-solution-w-images-explanation-bfs-dfs-o-1-optimized-bfs/
def get_none_sep_level_list(bt_root):
    result = []
    q = deque([bt_root])

    # while any items exist in queue
    while(q):
        # loop number of times == the length of queue RIGHT NOW - does not change even though we will be adding to queue in this loop
        for _ in range(len(q)):
            cur_node = q.popleft()
            result.append(cur_node.value)

            # add children of cur_node to queue for next time we re-eval range(len(q)) (for next "level" of tree) IF they exist
            if cur_node.left_node:
                q.append(cur_node.left_node)
            if cur_node.right_node:
                q.append(cur_node.right_node)
        
        # reached "end" of "level"
        result.append(None)
    return result






test_list = [1,2,3,4,5,6,7]

bt_root = list_to_binary_tree(test_list)
print(bt_root)

# step 2
print(f"{print_flattened_values(bt_root)=}")


print("\nSTEP 3 get_in_order_for_level():")
print(f"{get_in_order_for_level(bt_root,0)=}")
print(f"{get_in_order_for_level(bt_root,1)=}")
print(f"{get_in_order_for_level(bt_root,2)=}")
print(f"{get_in_order_for_level(bt_root,3)=}")

print("\nSTEP 4 get_none_sep_level_list(bt_root):")
print(f"{get_none_sep_level_list(bt_root)=}")

