def high_and_low(numbers):
    num_list=numbers.split()
    num_list_int=num_list
    for i in range(0,len(num_list)):
        num_list_int[i]=int(num_list[i])
    high=max(num_list_int)
    low=min(num_list_int)
    a=str(high)+' '+str(low)
    return a


#a=high_and_low('11 222 -3 23')
#print(a)
