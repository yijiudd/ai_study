
from textblob import TextBlob

posmessages=[]
negmessages=[]
#Open the .txt file in Python and extract the contents as a string
with open(r'D:\workspace\ai_study\nlp\pp.txt', "r",encoding='utf-8') as file:
    text = file.read()
#Create a TextBlob using the book string
blob = TextBlob(text)
#Analyse each sentence in the book in a loop
for sentence in blob.sentences:
    if sentence.sentiment.polarity==1:
        posmessages.append(sentence)
    elif sentence.sentiment.polarity==-1:
        negmessages.append(sentence)

#Print the most positive and most negative sentences
print("Most positive sentence: ",posmessages,'number:',len(posmessages))
print('-------------------')
print("Most negative sentence: ",negmessages,'number:',len(negmessages))