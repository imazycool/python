
str_input ="ajay"
tuple_input = ("a", "j", "a", "y")
list_input = ["a", "j", "a", "y"]
dict_input = {"a": 1, "j": 2, "a": 3, "y": 4}


#program to reverse the string using slicing and loop 
class RevString:
    
    def rev_string(self, input):
        print(input[::-1])
        
    def rev_str(self, input):
        rev_str=""
        for i in range(len(input)):
            rev_str+= input[len(input)-i-1]
        print(rev_str)
    
    def __init__(self, input):
        self.rev_string(input)
        self.rev_str(input)
        

RevString(str_input) 
RevString(tuple_input) 
RevString(list_input) 
# RevString(dict_input) 

