fv=[]
th=[]
def threetofive():
    thi=1
    fvi=1
    
    while thi*3<1000:
        #print(thi)    
        th.append(thi*3)
        thi+=1
    
    #print(th)

    while fvi*5<1000:
        #print(thi)    
        fv.append(fvi*5)
        fvi+=1
    
    #print(fv)
        
    #result =
    #print(result)
    #sum=0

    #for ele in range(0, len(result)):
    #    sum = sum + result[ele]
    result=sum(set(fv+th))
    print(result)

    return
threetofive()
