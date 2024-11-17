class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:

    def serialize(self, root):
        encoded = []

        def dfs(node):
            if not node:
                encoded.append("N")
                return
            encoded.append(str(node.val))
            dfs(node.left)        
            dfs(node.right)

        dfs(root)

        return ",".join(encoded)


    def deserialize(self, data):
        decoded = data.split(",")
        i = 0
        def dfs():
            nonlocal i

            value = decoded[i]
            i += 1        
            if value == "N":
                return None
            else:
                node = TreeNode(int(value))
                node.left = dfs()
                node.right = dfs()
                return node
            
        return dfs()
