# Trie Yourself
The `trie.py` file contains methods that allow for the use of a trie data structure to store words. The included methods allow for adding, searching, and suggestions of similiar words given the word's prefix. 

Tests are included in `trie_test.py` if additional functionality such as editing words are to be implemented and tested later. 

## Using a Trie
The trie can simply be instantiated using `Trie()`. This will create an empty data structure. Adding words to the trie is easily done by calling the `insert()` method on the trie.

### Sample Use

```
t = Trie()
t.insert('tulip')
t.search('tulip')
```

This will return `True` as tulip was inserted into the trie. 

The words in the trie are case sensitive and can include any character that is hashable.

```
t = Trie()
t.insert('Turkey')
t.search('turkey')
```

This snippet will return `False` because the Trie structure is implemented to be case sensitive.

## Instantiating a Trie With a Vocabulary List
The trie's constructor can take a list of words as an optional parameter which will instantiate the trie with that vocabulary list.

```
t = Trie(['apple', 'banana', 'casava', 'dolichuric'])
t.search('casava')
```

This snippet will return `True` as the constructor has built the trie using the list of words provided to the constructor.

## Autocomplete
The trie structure is fantastic for autocompleting based on a prefix of a word.

```
t.Trie(['dozy', 'doll', 'dollar', 'dollarbird'])
t.autocomplete('dol')
```

This snippet will return a list of all words that begin with the prefix `dol`.

```
['doll', 'dollar', 'dollarbird']
```

The word `dozy` is left out because it doesn't contain the prefix.

## Benchmarks
The trie data structure is extraordinarily quick to build.

The initial setup using a dictionary of 235,886 words takes a mere 0.000005 sec. 

Running the autocomplete function on the built trie is several orders of magnitude slower however. Here are the runtimes for different autocomplete suggestions using the autocomplete benchmarking script included in this repository.

Running `python autocomplete s` will return every word that begins with s with the following benchmarks:

```
Initial setup time: 0.000005 sec
Autocomplete time:  0.032807 sec
Total time elapsed: 0.032812 sec
```

Running `python autocomplete xanthod` will output a much smaller list of results as follows:

```
Vocabulary size: 235886
Completions of xanthod: xanthoderm, xanthoderma, xanthodont, xanthodontous

Initial setup time: 0.000004 sec
Autocomplete time:  0.029575 sec
Total time elapsed: 0.029579 sec
```

Finally, benchmarking more common autocomplete prefixes such as 'stupe' returns a similar result to the following example.

```
Vocabulary size: 235886
Completions of stupe: stupe, stupefacient, stupefaction, stupefactive, stupefactiveness, stupefied, stupefiedness, stupefier, stupefy, stupend, stupendly, stupendous, stupendously, stupendousness, stupent, stupeous, stupex

Initial setup time: 0.000005 sec
Autocomplete time:  0.030520 sec
Total time elapsed: 0.030525 sec
```