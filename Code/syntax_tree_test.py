from syntax_tree import ASTree

def test_init():
  t = ASTree()
  assert t.root == None
 

def test_insert():
  t = ASTree()

  t.parse("3+4*5")
  t.parse("23+56*2")

  t.parse("2+ 4")
  assert t.root.symbol == "+"
