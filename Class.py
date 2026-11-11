class Data:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def get_data(self):
    return (self.a+self.b)
obj=Data(2,4)
result=obj.get_data()
print(result)
#Average caluctlator using class
class Calculator:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    def CalculateAverage(self):
        Average=(self.num1 + self.num2 + self.num3)/3
        print(f"The average of 10, 20, and 30 is {Average}")
obj=Calculator(10,20,30)
obj.CalculateAverage()