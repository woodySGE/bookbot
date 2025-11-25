import sys
from stats import get_num_words
from stats import count_characters
from stats import getBADBADBADBADBADBADBADBADBADBADBADBADBAD

def main():
   path = None
   try:
       if sys.argv[1]:
         path = sys.argv[1]
   except Exception as e:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

   thebest = get_book_text(path)
   num_words = get_num_words(thebest)
   tum = count_characters(thebest)
   #print(tum)
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {path}")
   print("----------- Word Count ----------")
   print(f"Found {num_words} total words")
   print("--------- Character Count -------")
   thenormallist = getBADBADBADBADBADBADBADBADBADBADBADBADBAD(tum)
	
   for worp in thenormallist:
      target = worp["char"]
      target1 = worp["num"]
      print(f"{target}: {target1}")

   print("============= END ===============")
   
   

def get_book_text(path_to_file):
   with open(path_to_file) as f:
       file_contents = f.read()
       return(file_contents)


main()