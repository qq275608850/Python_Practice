
def spin_words(sentence):
    arr=[a for a in sentence.split(" ")]
    m=[]
    for i in arr:
        if len(i)>=5:
            m.append(i[::-1])
        else:
            m.append(i)
    res=" ".join(a for a in m)
    return res
