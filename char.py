string="sushma is a good girl"
char=0
word=1
for i in string:
    char=char+1
    if(i==''):
        word=word+1
        print("number of wirds in the string:")
        print(word)
        print("number of characters in the string:")
        print(char)
