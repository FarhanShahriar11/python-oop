class students:
    def __init__(self,name,id) -> None:
        self.name=name
        self.__id=id
    def view(self):
        print(self.name,self.__id)
x=students('farhan',20)
x.view()
#####################################
class Student:
    
    def __init__(self,name, Id):
        self.name=name
        self.__id = Id
       
    def details(self):
        print("name",self.name, "Id", self.__id)
    def set_id(self,Id):
        if(Id>0):
            self.__id=Id
        else:
            print("Enter valid number")
    def get_id(self):
         print(self.__id)
        # return self.__id

s=Student("hasan", 10)
s1=Student("farhab",11)
s2=Student('rakib',12)

s.set_id(110)
s.get_id()
s.details()