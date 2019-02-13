#!python
from trie import Trie
 

def test_insert():
  t = Trie()
  t.insert("Apogee")
  assert t.root.children['A']
  assert t.root.children['A'].children['p'].children['o'].children['g'].children['e'].children['e']
  assert t.root.children['A'].children['p'].children['o'].children['g'].children['e'].children['e'].word_end

def test_search():
  t = Trie()
  t.insert("Astral")
  assert t.search("Astral")
  assert not t.search("Papaya")

def test_find_similar():
  t = Trie()
  t.insert("Rollercoaster")
  t.insert("Roll")
  t.insert("Rollerama")
  values = t.find_similar("Roll")
  for value in ['rollercoaster', 'roll', 'rollerama']:
    assert value in values