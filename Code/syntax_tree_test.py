from syntax_tree import ASTree

def test_init():
  t = ASTree()
  assert t.root == None
 

def test_insert():
  t = ASTree()

  t.parse("348+47*5501")
  assert t.root.symbol == '+'
  assert t.root.left.value == "348"
  assert t.root.right.value == None
  assert t.root.right.symbol == "*"

  t.parse("23+56*2")

  t.parse("2+ 4")
  assert t.root.symbol == "+"

def test_evaluate():
  t = ASTree()
  t.create_test_tree()
  evaluated_answer = t.evaluate()
  print("Answer: {}".format(evaluated_answer))
  assert evaluated_answer == float(31)