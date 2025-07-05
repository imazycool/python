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
    
    def lambda_func_filter_even(input):
        result_even = list ( filter( lambda x: x%2 ==0 , input))
        result_odd = list ( filter( lambda x : x%2 != 0 ,input )) 
        print( "even numbers are --> " , result_even )
        print("odd numbers are --> " , result_odd )
    
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

#filter even and odd numbers from the given list 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
use_lambda.lambda_func_filter_even(my_list) 
result=list(filter(lambda x : x%2==0 , my_list))
print("even numbers from my list : " , result )
result=list(filter( lambda x: x%2!=0 , my_list))
print("odd numbers are from my list : ", result)


##Python program to square and cube every number in a given list of integers using Lambda.
## map functio use to stream the values from list 
my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=map(lambda x : x**2,my_list) 
print(list(result))


##Python program to find if a given string starts with a given character using Lambda.
## condition handelling inside lambda function 
my_str="this is sample string text"
result=lambda x,y: True if x.startswith(y) else False 
print(result(my_str,"t"))


## format date to string and string to date 
from datetime import datetime 
my_str_time="2025-07-01"
my_date_time= "2025-06-11 20:59:00"
result= lambda x: datetime.strptime(x, '%Y-%m-%d')
print(result(my_str_time).year)


## program to check whether a given string is a number or not using Lambda.
my_list=[1, 2.4 , 3, "ajay", 5, "arsh", 7, "jk" , 9, 10]
result= map(lambda x : True if type(x) in (int,float )   else False, my_list) 
print(list(result)) 

#lambda nested conditions 
n=[ 0,1,2,3,4,5,6,7,8,9,11,112,1212,134]
result= map(lambda x : "FizzBuzz" if (x%3==0 and x%5==0) else "Fizz" if (x%3==0) else "Buzz" if (x%5==0) else x , n ) 
print(list(result))
print(map(int , n))