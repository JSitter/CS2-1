#! /usr/bin/env python3

class ASTree():
  def __init__(self, math_expression=None):
    self.root = None

    if math_expression:
      self.parse(math_expression)
  
  def parse(self, values):
    '''
    This function takes a valid string of valid mathematical expressions and builds an Abstract Syntax Tree to evaluate it.
    '''
    #Clear out old Tree
    self.root = None

    valid_operators = {
      "+":True, 
      "-":True, 
      "/":True, 
      "*":True,  
      }

    values = values.replace(' ', '')
    index = 0
    cur_number = []
    cur_node = None

    while index < len(values):

      if values[index] in valid_operators:
        new_node = ASNode(symbol=values[index])
        print("Number: {}".format("".join(cur_number)))
        print("Operator: {}".format(values[index]))
        cur_number = []
      else:
        cur_number.append(values[index])
      index += 1
      if index == len(values):
        print("At end of list of values: {}".format("".join(cur_number)))
    
  def create_test_tree(self):
    '''
    Creates Test Tree

         +
        / \
      3    *
          / \
         4   7

      Should evaluate to 31 and not 49
    '''
    self.root = ASNode(symbol = "+")
    self.root.left = ASNode(value="3")
    self.root.right = ASNode(symbol='*')
    self.root.right.left = ASNode(value="4")
    self.root.right.right = ASNode(value="7")


  def evaluate(self, node=None):
    '''
    This method will recursively evaluate an abstract syntax tree and return the calculated value.
    '''
    if node == None:
      node = self.root

    if node.value is not None:
      return float(node.value)
    
    if node.symbol == "+":
      return self.evaluate(node.left) + self.evaluate(node.right)
    elif node.symbol == "-":
      return self.evaluate(node.left) - self.evaluate(node.right)
    elif node.symbol == "*":
      return self.evaluate(node.left) * self.evaluate(node.right)
    elif node.symbol == "/":
      return self.evaluate(node.left) / self.evaluate(node.right)
    

  
class ASNode():
  def __init__(self, value=None, symbol=None):
    self.value = value
    self.symbol = symbol
    self.left = None
    self.right = None  
