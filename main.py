from stats import count_words
from stats import count_chars
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main(filepath):
    ##print(get_book_text(filepath))
	##print(count_chars(filepath))
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}")
	print("----------- Word Count ----------")
	print(count_words(filepath))
	print("--------- Character Count -------")
	print(count_chars(filepath))

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		main(sys.argv[1])
