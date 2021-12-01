
구구단=[]
for a in range(1,10):
    for i in range(1,10):
        구구단.insert(i,a*i)   
        
        if i ==9:
            print(*구구단)     
            list.clear(구구단)
print ("uploading")