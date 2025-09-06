def word_count (content):
    wordArray = content.split()
    return len(wordArray)

def stats(content):
    char_dict = {}
    for c in content:
        c = c.lower()
        if c in char_dict:
            char_dict[c] += 1
        else: 
            char_dict[c] = 1
    return char_dict

def sorton(item):
    return item["num"]

def sorted_dict(char_dict):
    arraydict = []
    
    for item in char_dict.items():
        if item[0].isalpha():
            arraydict.append( {"char":item[0], "num":item[1]})
    
    arraydict.sort(reverse=True, key=sorton)
    return arraydict
