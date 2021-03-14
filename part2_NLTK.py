from nltk.book import * 

#thie function is to remove all punctuation
#namely, only retain the characters 'a-z', 'A-Z' and '0-9'
#anything else will be replaced by ' ' (space)
def removePunctuation(item):
    texts = ""
    for everyChar in item:
        if everyChar>='a' and everyChar<='z':
            texts = texts + everyChar
        elif everyChar>='A' and everyChar<='Z':
            texts = texts + everyChar
        elif everyChar>='0' and everyChar<='9':
            texts = texts + everyChar
        else:
            texts = texts + ' '
    return texts.strip() #also remove the spaces at the beginning and the end


#to lower the case after removing all punctuation
def lowercaseWords(item):
    #remove the spaces at the beginning and the end
    item = item.strip()
    return item.lower()


#use a dictionary to store all words
#the key is the word, and value is its frequency
record = {}

#get how many different words in text7
size = len(text7)

#iterate text7
i = 0
while i < size:
    item = text7[i] #get the nth word
    item = removePunctuation(item) #remove all punctuation
    its = item.split(' ') #splt with space, then it will be list
    for v in its:
        if len(v) == 0: #empty word
            continue
        v = lowercaseWords(v) #lowercase
        #store it in the dictionary
        if v not in record:
            record[v] = 1
        else:
            record[v] = record[v] + 1
    i = i + 1

#sort is by descending order
record = sorted(record.items(),key=lambda x:x[1],reverse=True)
#print(record)

#print the top 50
i = 0
while i < 50:
    print(record[i])
    i = i + 1

















    
