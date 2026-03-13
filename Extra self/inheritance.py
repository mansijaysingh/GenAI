class Employee:
  def __init__(self, name ,id):
    self.name=name
    self.id=id
  
  def show_detail(self):
    print(f"employee name is {self.name} and his id is {self.id}")



class Programmer(Employee):
  def show_langauge(self):
    print("the defualt language is python")



e1=Employee("Harry",200)
e1.show_detail()
e1.name="harshit"
e1.show_detail()

e2=Programmer("Ashish",250)
e2.show_detail()
e2.show_langauge()