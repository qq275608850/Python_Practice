
def duplicate_count(text):
    # Your code goes here
    new_text = text.lower()
    count = 0
    dictionary = {}
    for i in range(0,len(new_text)):
#        print(len(new_text))
        dictionary[new_text[i]] = 0
#        print(dictionary)
    for key in dictionary:
#        print(key)
        for i in range(0,len(new_text)):
#            print(len(new_text))
            if(key == new_text[i]):
                dictionary[key] = dictionary[key] + 1               
#                print(dictionary)
    for key in dictionary:
        if(dictionary[key] > 1):
            count = count + 1

    print(dictionary)
    return count

#a=duplicate_count('achACH1')
#print(a)
