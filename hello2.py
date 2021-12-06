class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second=second
        #init 처음으로 실행 (무조건)
    def add(self):
        result = self.first +self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result=self.first**self.second
        return result
    def add(self):
        print("자식")

a=MoreFourCal(1,2)
#a.setdata(4,2)
print(a.add())
