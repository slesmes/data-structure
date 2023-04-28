from binary_tree import BinaryTree
tree= BinaryTree(20)
tree.insert(tree,BinaryTree(16))
tree.insert(tree,BinaryTree(21))
tree.insert(tree,BinaryTree(18))
tree.insert(tree,BinaryTree(23))
tree.insert(tree,BinaryTree(15))
tree.insert(tree,BinaryTree(22))
tree.print_tree(tree)