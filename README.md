# BookBot

BookBot is a small CLI app that analyzes a text file and prints:

1. Total word count
2. Character frequency report (letters only), sorted highest to lowest

## Requirements

- Python 3

## Usage

```bash
python3 main.py <path_to_book>
```

Example:

```bash
python3 main.py books/frankenstein.txt
```

If you run it without a file path, it prints:

```text
Usage: python3 main.py <path_to_book>
```

and exits with status code `1`.

## Sample output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
...
============= END ===============
```