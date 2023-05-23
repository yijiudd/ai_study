from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
# import and create a Conll extractor to use later 
extractor = ConllExtractor()
print("""Hello, I am Marvin, the simple robot.
You can end this conversation at any time by typing 'bye'
After typing each answer, press 'enter'
How are you today?""")
while True:
    input_str = input('> ')
    if(input_str == 'bye'):
        print('Bye!')
        break
    input_blob=TextBlob(input_str, np_extractor=extractor)
    if input_blob.polarity<=-0.5:
        response = "Oh dear,that sounds bad. "
    elif input_blob.polarity<=0:
        response = "Hmm, that's not great. "
    elif input_blob.polarity<=0.5:
        response = "Well, that sounds positive. "
    elif input_blob.polarity<=1:
        response = "Wow,that sounds great. "
    
    #If a noun phrase is detected in the sentiment, pluralize it and ask for more input on that topic
    if len(input_blob.noun_phrases)>0:
        response = response + "Can you tell me more about " + input_blob.noun_phrases[0]+'s' + "?"
    else:
        response = response + "Can you tell me more?"
    print(response)    
    

    
