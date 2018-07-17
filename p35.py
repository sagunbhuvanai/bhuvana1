class A:
    a=10
    b=20
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print('init is invoked')
    def display(self):
        print('name ->',self.name)
        print('age ->',self.age)
        print('address ->',self.address)
obj=A('bhuvi',22,'hubli-dharwad')
obj.display()

