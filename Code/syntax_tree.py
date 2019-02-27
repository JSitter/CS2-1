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
      "^":True, 
      "(":True, 
      ")":True
      }

    values = values.replace(' ', '')
    index = 0
    cur_number = []

    while index < len(values):

      if values[index] in valid_operators:

        print("Number: {}".format("".join(cur_number)))
        print("Operator: {}".format(values[index]))
        cur_number = []
      else:
        cur_number.append(values[index])
      index += 1
      if index == len(values):
        print("At end of list of values: {}".format("".join(cur_number)))
    
     

  def evaluate(self):
    '''
    This method will evaluate the abstract syntax tree and return the calculated value.
    '''
    pass

  
class ASNode():
  def __init__(self, value=None,  symbol=None):
    self.symbol = value
    self.value = value
    self.left = None
    self.right = None  
