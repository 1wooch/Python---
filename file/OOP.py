class Car():

  def __init__(self,**kwargs):
    self.wheels=4
    self.doors=4
    self.windows=4
    self.seats=4
    self.color=kwargs.get("color","black")
    self.price=kwargs.get("price","20$")

  def __str__(self):
    return f"Car with {self.wheels}wheels"

  def take_off(self):
    return "taking off"

class convertable(Car):
    def __init__(self,**kwargs):
        super().__init__(**kwargs) #call father class (where i got inherit) so .get dont need to delete all the element
        self.time= kwargs.get("time",10) #delete init and replace only tieme
    def take_off(self):
        return "taking off" 
    def __str__(self):
        return f"Car with no roof"
class Something(convertable):
    pass

porche=convertable(color="green",price="$40")
print(porche.time)