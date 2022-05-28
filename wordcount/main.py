# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content():
  file = open("story.txt", "r")
  contents = file.read()    
  print(contents)


read_file_content()



def count_words():
  file = open("story.txt", "r")
  counts = dict()
  
  for line in file:
    words = line.split()
    for word in words:
      if word in counts:
        counts[word] += 1
      else:
          counts[word] = 1
  print (counts)
  
count_words()





