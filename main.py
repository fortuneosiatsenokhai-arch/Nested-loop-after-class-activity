word=input("enter a word: ")
letter=input("enter a letter: ")
i=0
count=0

while (i<len(word)):
    if(word[i]==letter):
        count=count+1
    i=i+1
print(f"the total numbe that the letter '{letter}' has appeared in '{word}' is {count}")
