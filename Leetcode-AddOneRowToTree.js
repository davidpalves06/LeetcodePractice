
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
 
/**
 * @param {TreeNode} root
 * @param {number} val
 * @param {number} depth
 * @return {TreeNode}
 */
var addOneRow = function(root, val, depth) {
    if (depth == 1) {
        let leftNode = new TreeNode(val,root,null)
        return leftNode
    }

    function addNode(node,val,depth,direction) {
        if (depth == 1) {
            if (direction == 0) {
                let leftNode = new TreeNode(val,node,null)
                return leftNode
            }
            else {
                let rightNode = new TreeNode(val,null,node)
                return rightNode
            }
        }

        if (node == null) return null
        let leftNode = addNode(node.left,val,depth - 1,0);
        if (leftNode != null) node.left = leftNode
        let rightNode = addNode(node.right,val,depth - 1,1);
        if (rightNode != null) node.right = rightNode

        return null
    }

    let leftNode = addNode(root.left,val,depth - 1,0);
    if (leftNode != null) root.left = leftNode
    let rightNode = addNode(root.right,val,depth - 1,1);
    if (rightNode != null) root.right = rightNode

    return root
};