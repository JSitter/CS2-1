#! python3

class Trie:
  def __init__(self, vocabulary=[]):
    self.root = Trie_Node()
    for word in vocabulary:
      self.insert(word)

  def insert(self, word):
    cur_node = self.root
    for index, char in enumerate(word):
      if char in cur_node.children:
        # Descend into child node
        cur_node = cur_node.children[char]
        if len(word) - 1 == index:
          cur_node.word_end = True
      else:
        # Add character as child
        new_node = Trie_Node()
        if len(word) - 1 == index:
          new_node.word_end = True
        cur_node.children[char] = new_node
        cur_node = cur_node.children[char]
  
  def search(self, word):
    cur_node = self.root
    for index, char in enumerate(word):
      if char in cur_node.children:
        # Last character of word should have a flag set
        if len(word) - 1 == index:
          if cur_node.children[char].word_end:
            return True
          else:
            return False
        else:
          # Not at last character yet
          cur_node = cur_node.children[char]
      else:
        # Character index doesn't exist -- return false immediately 
        return False

  def autocomplete(self, prefix):
    cur_node = self.root
    words = []
    for char in prefix:
      if char in cur_node.children:
        cur_node = cur_node.children[char]
      else:
        # Haven't gotten to end of prefix therefore no similar words exist
        return words
    
    return self.find_child_words(cur_node, prefix)
     
  def find_child_words(self, cur_node, prefix):
    words = []
    for char in cur_node.children:
      if cur_node.children[char].word_end:
        words.append("{}{}".format(prefix, char))
      words = words + self.find_child_words(cur_node.children[char], prefix+char)

    return words

class Trie_Node:
  def __init__(self):
    # End of word defaults to False
    self.word_end = False
    # Initialize starting values to None
    self.children = {}
