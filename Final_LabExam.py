from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def vertical_order_traversal(root):
    result = []

    if not root:
        return result

    vertical_dict = defaultdict(list)

    queue = deque()
    distance_queue = deque()

    queue.append(root)
    distance_queue.append(0)

    while queue:
        current = queue.popleft()
        distance = distance_queue.popleft()

        vertical_dict[distance].append(current.val)

        if current.left:
            queue.append(current.left)
            distance_queue.append(distance - 1)

        if current.right:
            queue.append(current.right)
            distance_queue.append(distance + 1)

    for values in sorted(vertical_dict.items()):
        result.extend(values[1])

    return result[::-1]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.right = TreeNode(9)

result = vertical_order_traversal(root)
print(result)
