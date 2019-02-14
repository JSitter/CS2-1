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
  t.insert("Ticonderoga")
  t.insert("aunt")
  t.insert("ant")
  t.insert("anteater")

  values = t.autocomplete("Roll")
  for value in ['Rollercoaster', 'Rollerama']:
    assert value in values