import re
calculator=[lambda a,b: a+b,lambda a,b:a-b ,lambda a,b : a*b , lambda a,b:a/b]

def start(str):
    #print(str)
    numbers = re.findall(r'\d+', str)
    firstnum=int(numbers[0])
    secondnum=int(numbers[1])
    #print(numbers[0].isdigit())
    #print(str)
    #print(numbers)
    #print(calculator[0],(12,13))
    if "+" in str:
        #print("+")
        
        print(calculator[0](int(numbers[0]),int(numbers[1])))
    if "-" in str:
        #print("-")
        
        print(calculator[1](firstnum,secondnum))
    if "*" in str:
             
        print(calculator[2](firstnum,secondnum))
    if "/" in str:
                
        print(calculator[3](firstnum,secondnum))   
   
#답=calculator[0](12,13)
#print(답)
start("12+13")
start("12-13")
start("12*13")
start("12/13")


