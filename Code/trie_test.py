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

def test_autocomplete():
  t = Trie()
  t.insert("rollercoaster")
  t.insert("roll")
  t.insert("rollerama")
  t.insert("ticonderoga")

  values = t.autocomplete("roll")
  for value in ['rollercoaster', 'rollerama']:
    assert value in values
  
  values = t.autocomplete("ro")
  for value in ['roll', 'rollercoaster', 'rollerama']:
    assert value in values