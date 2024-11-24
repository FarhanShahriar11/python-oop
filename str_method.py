class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def __str__(self):
        return(self.name,self.id)
s=employee("farhan",20)
print(s.__str__())
