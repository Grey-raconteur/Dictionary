import json

from difflib import get_close_matches


data = json.load(open("data.json"))

def meaning(word):
    if word in data:
        return data[word]
    else:   
        word = word.lower()
        if word in data:
            return data[word]
        elif len(get_close_matches(word, data.keys())) > 0:
            for i in range(9):
                yn = input("Did you mean %s instead ? \n Enter Y if Yes N if No " % get_close_matches(word, data.keys(), 10)[i])
                if yn != "Y" and yn != "N":
                    return "Please type again"
                if yn == "Y":
                    return data[get_close_matches(word, data.keys(), 10)[i]]
            if yn == "N":
                return "Word does not exist"


word = input("Enter the word ")
op = meaning(word)

    

if type(op) == list:
    for items in op:
        print(items)
else:
    print(op)


