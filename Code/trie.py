#! python3

class Trie:
  def __init__(self):
    self.root = Trie_Node()
  
  def char_to_index(self, character):
    char = character.lower()
    # ASCII A = 97 so subtract 97
    index = (ord(char) - 97)
    if index < 0 or index > 25:
      raise Exception('Character out of range: Words can only contain characters a-z.')
    return index
  
  def insert(self, word):
    cur_node = self.root
    for index, char in enumerate(word):
      # returns True if character already appears
      char_index = self.char_to_index(char)
      if cur_node.children[char_index]:
        # Descend into child node
        cur_node = cur_node.children[char_index]
        if len(word) - 1 == index:
          cur_node.word_end = True
      else:
        # Add character as child
        new_node = Trie_Node()
        if len(word) - 1 == index:
          new_node.word_end = True
        cur_node.children[char_index] = new_node
        cur_node = cur_node.children[char_index]
  
  def search(self, word):
    cur_node = self.root
    for index, char in enumerate(word):
      char_index = self.char_to_index(char)
      # Last character of word should have a flag set
      if len(word) - 1 == index:
        if cur_node.children[char_index].word_end:
          return True
        else:
          return False
      else:
        # Not at last character yet
        if cur_node.children[char_index]:
          cur_node = cur_node.children[char_index]
        else:
          # Character index doesn't exist return false immediately 
          return False


  def autocomplete(self, prefix):
    cur_node = self.root
    words = []
    for char in prefix:
      char_index = self.char_to_index(char)
      if cur_node.children[char_index]:
        cur_node = cur_node.children[char_index]
      else:
        # Haven't gotten to end of prefix therefore no similar words exist
        return words
    # Find all child words
    for char in cur_node.children:
      chars = ""
  
  def find_all_child_words(self, cur_node, prefix):
    pass

class Trie_Node:
  def __init__(self):
    # End of word defaults to False
    self.word_end = False
    # Initialize starting values to None
    self.children = [None] * 26
