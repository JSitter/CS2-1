#!python
from trie import Trie

def test_char_to_index():
  t = Trie()
  assert t.char_to_index('a') == 0
  assert t.char_to_index('A') == 0
  assert t.char_to_index('Z') == 25
  

def test_insert():
  t = Trie()
  t.insert("Apogee")
  assert t.root.children[0]

def test_search():
  t = Trie()
  t.insert("Astral")
  assert t.search("astral")
  assert not t.search("Papaya")

def test_find_similar():
  t = Trie()
  t.insert("Rollercoaster")
  t.insert("Roll")
  t.insert("Rollerama")
  values = t.find_similar("roll")
  for value in ['rollercoaster', 'roll', 'rollerama']:
    assert value in values