# #non-parameter constructor

# class people:
#     def __init__(self) -> None:
#         print("my name is farhan")
# s=people()

# #parameter constructor

# class people:
#     def __init__(self,name) -> None:
#         self.name=name
#         print(self.name)
# s=people("farhan")

#instance object

# class people:
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.age=age
#     def view(self):
#         print(self.name,self.age)
# s=people('Rakib',24)
# s.view()
class Animal(object):
  def __init__(self, animal_type):
    print('Animal Type:', animal_type)
    
class Mammal(Animal):
  def __init__(self):

    # call superclass
    super().__init__('Mammal')
    # print('Mammals give birth directly')
    
dog = Mammal()

