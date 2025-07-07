class Parent_class:

    #default value class initiliaze 
    def __init__(self,int_length=4, int_width=7 ):
        print("********  inside parent class *******")
        self.length= int_length
        self.width= int_width 

    def area_square(self):
        return self.length* self.length

    def area_rectangle(self):
        print("area od square --> " , self.length*self.width )
        return self.length*self.width 
    

## child class 
class Child_class(Parent_class) :
    
    def __init__(self,int_length=6, int_width=4 ):
        self.length= int_length
        self.width= int_width 
        
# creating obj instance with default values 
obj_01=Parent_class()
print(obj_01.area_rectangle())


class My_class:
    def __init__(self):
        self.x,self.y=5,10 
        
    def add(self): return self.x + self.y

obj_02=My_class()
print("class demo--> ", obj_02.add())


class var_test:
    var_01="ajay variable displayed in class"
    
    def __init__(self):
        print("class initialized")
        self.var_01="new_value from class init"
    
    def func_var(self):
        print("")
        return self.var_01

obj_01= var_test()
print(obj_01.func_var())
