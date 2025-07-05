class use_lambda:
        
    #Add 10 to argument a, and return the result:
    def lambda_func_01(input):
        result = lambda a:a+10
        print(result(input))
    
    #Multiply argument a with argument b and return the result:
    def lambda_func_02(input1, input2):
        result=lambda a,b:a*b
        print(result(input1, input2))
    
    #Use that function definition to make a function that always doubles the number you send in:
    def lambda_func_03(n):
        result= lambda a : a * n 
        print(result(2))
    
    ##program to sort a input 
    def lambda_func_list_only(input):
        print("input type is --> " , type(input))
        if (type(input) == list):
            input.sort(key =lambda x:x[1])
            result=input
        else:
            result =  sorted(input)
        print (result)
    
    #program to sort a list of dictionaries items by a key_key 
    def lambda_func_list_dict(input, key_key):
        input_type= type(input[0])
        print("item type is --> " , input_type )
        if (input_type == dict):
            result = sorted(input , key =lambda x : x[key_key])
        print(result) 
        
    
    def __init__(self,input):
        # self.lambda_func_01(input)
        print("result displayed below")
        
        
# Add 10 to argument a, and return the result:
use_lambda.lambda_func_01(3)

# Multiply argument a with argument b and return the result:
use_lambda.lambda_func_02(7 , 13)

#Use that function definition to make a function that always doubles the number you send in:ß
use_lambda.lambda_func_03(9)

#Python program to sort a list of tuples using Lambda.
#Original list of tuples:
my_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
use_lambda.lambda_func_list_only(my_list)

# for sorting list of dictionaries 
my_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
           {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
use_lambda.lambda_func_list_dict(my_dict,"make")



