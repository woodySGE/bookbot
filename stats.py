def get_num_words(thebest1):
   num_words1 = thebest1.split()
   num_words = len(num_words1)
   return(num_words)

def count_characters(stuff):
   newlist = {}
   get_characters = stuff.lower()
   gorb = get_characters.split(" ")
   for er in get_characters:
      if (er not in newlist):
        newlist[er] = 0
      if (er in newlist):
        newlist[er] += 1
   return(newlist)

def getBADBADBADBADBADBADBADBADBADBADBADBADBAD(tum):
   thenormallist = []
   for tub in tum:
      theworstlist = {}
      theworstlist["char"] = tub
      theworstlist["num"] = tum[tub]
      thenormallist.append(theworstlist)

   return(thenormallist)
