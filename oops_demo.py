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



