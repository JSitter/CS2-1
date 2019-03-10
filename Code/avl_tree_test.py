from avl_tree import AVL_Tree, AVL_Node

def test_init():
  t = AVL_Tree()
  assert t.root == None

def test_insert():
  t = AVL_Tree()
  fog_node = AVL_Node("fog")
  frog_node = AVL_Node("frog")
  log_node = AVL_Node("log")
  nog_node = AVL_Node("nog")
  prague_node = AVL_Node('prague')
  rag_node = AVL_Node('rag')
  sog_node = AVL_Node('sog')


  t.insert(fog_node)
  assert t.root.value == fog_node.value

  t.insert(frog_node)
  assert t.root.right.value == frog_node

  t.insert(log_node)
  assert t.root.value == frog_node.value
  assert t.root.left.value == fog_node.value
  assert t.root.right.value == log_node.value

  t.insert(nog_node)
  assert t.root.right.right.value == nog_node.value

  t.insert(prague_node)
  


