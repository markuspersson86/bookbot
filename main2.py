#print("hello world")

def PrintContent():
        # prints whole content of book
     with open("books/frankenstein.txt") as f:
         file_contents = f.read()
         return file_contents


def CountWords():
    count=0
    stringList=[]
        #count number of words
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        stringList = file_contents.split()
        
        count = len(stringList)

        print(count, "words found in the document")

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def main():
   text = ""
   text= PrintContent()
   CountWords()
   chars_dict = get_chars_dict(text)
    #prints dictionary with number of each character
   # print(chars_dict)

   alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
   
   for c in chars_dict:
     if(c in alphabet):
        print("The",str(c),"character was found",chars_dict[c],"times")
main()