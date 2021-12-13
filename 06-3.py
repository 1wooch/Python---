import math

def page(m,n):
    if(m<n):

        if(m%n==0):
            numberpage=m/n
            print(numberpage)

        else:
            numberpage=math.floor(m/n)+1
            print(numberpage)
    else:
        print(1)
    return

page(15,5)

print(15//15)