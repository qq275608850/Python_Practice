def likes(names):
    if  len(names) == 0:
        a='no one likes this'
    elif len(names) == 1:
        a='%s likes this'%names[0]
    elif len(names) ==2:
        a='%s and %s like this'%(names[0],names[1])
    elif len(names) == 3:
        a='%s, %s and %s like this'%(names[0],names[1],names[2])
    else:
        a='%s, %s and %d others like this'%(names[0],names[1],len(names) - 2)
    return a
