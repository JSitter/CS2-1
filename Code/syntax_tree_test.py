from syntax_tree import ASTree

def test_init():
  t = ASTree()
  assert t.root == None
 
def test_parse_single_addition():
  t = ASTree()
  t.parse("2+3")
  assert t.root.symbol == "+"
  assert t.root.left.value == "2"
  assert t.root.right.value == "3"

def test_evaluate_single_addition():
  t = ASTree("4+5")
  assert t.evaluate() == float(9)

def test_parse_multi_addition():
  t = ASTree()
  t.parse("2+3+5")
  assert t.root.symbol == "+"
  assert t.root.left.symbol == "+"
  assert t.root.right.value == "5"
  assert t.root.left.left.value == "2"
  assert t.root.left.right.value == "3"

def test_parse_multi_varied():
  t = ASTree()

  t.parse("348+47*5501")
  assert t.root.symbol == '*'
  assert t.root.right.value == "5501"
  assert t.root.left.symbol == "+"
  assert t.root.left.value == None
  

  t.parse("23+56*2")

  t.parse("2+ 4")
  assert t.root.symbol == "+"

def test_evaluate_multi_varied():
  t = ASTree()
  t.parse("47*5501+348")
  assert t.evaluate() == float(258895)

def test_evaluate():
  t = ASTree()
  t.create_test_tree()
  evaluated_answer = t.evaluate()
  print("Answer: {}".format(evaluated_answer))
  assert evaluated_answer == float(31)