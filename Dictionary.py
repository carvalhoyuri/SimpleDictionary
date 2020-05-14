import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
         return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yorn = input( "Try again. Did you mean %s instead? Type Y if yes or N if No: " %get_close_matches(w, data.keys())[0] )
        if yorn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yorn =="N":
            return "The word doesn't exist. Please double check it"
        else:
            return "Sorry, I didn't understand your entry."
    else: 
        return "The word doesn't exist. Please double check it"
    



word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)