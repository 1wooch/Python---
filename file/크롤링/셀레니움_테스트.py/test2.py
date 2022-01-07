class Myswitch:
    def switch(self,arg): #arg=0
        print(arg)
     
        self.case_name="case_"+str(arg)
        

        
        self.case=getattr(self,self.case_name,lambda:"default")
        print(self.case)
        return self.case()
       
    def case_서울(self):
        print('1')
       
        
    def case_1(self):
        print("2")    
    def case_2(self):
        print("3")
    def case_default(default):
        print("default")

obj=Myswitch()
obj.switch("서울")