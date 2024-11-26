class student:
    uni_name='stf'
    def __init__(self,name) -> None:
        self.name=name
    def view(self):
        print(self.name,student.uni_name)
    @classmethod
    def update(cls,u_name):
        cls.uni_name=u_name
s=student('farhan')
s.view()
s.update("stamford")
s.view()

###static method
