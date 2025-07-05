
str_input ="ajay"
tuple_input = ("ajay", "singh", "rajpoot", "imazy" , 5 , 12, 33 , 45)
list_input = ["ajay", "jitesh", "anurag", "arsh" , "rajpoot", 5, 12, 33, 45]
dict_input = {"name": "ajay" , "surname": "rajpoot", "age": 40 }


#program to reverse the string using slicing and loop 
class RevString:
    
    def rev_string(self, input):
        print(input[::-1])
        
    def rev_str(self, input):
        rev_str=""
        for i in range(len(input)):
            rev_str+= input[len(input)-i-1]
        print(rev_str)
    
    def func_reverse_word(str_input):
        for i in range(len(str_input)-1,-1,-1):
            print(str_input[i] , end="")
        print("")
    
    def __init__(self, input):
        self.rev_string(input)
        self.rev_str(input)
        

RevString(str_input) 
# RevString(tuple_input) 
# RevString(list_input) 
# RevString(dict_input) 


class Slicing:
    
    def slice_tuple(self, input): 
        print(input[2:5])
        
    def slice_list(self,input):
        print(input[2:5])
        
    def slice_dict(self, input):
        print(input["name"][::-1], input["surname"][::-1], input["age"])
    
    def __init__(self, input):
        # self.slice_tuple(input)
        # self.slice_list(input)
        self.slice_dict(input)

# Slicing(tuple_input)
# Slicing(list_input)
Slicing(dict_input)