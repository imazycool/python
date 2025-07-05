class Operations:
    #initiate class 
    def __init__(self,input):
        print("class initiated")
        
    def func_01(start_number,end_number):
        result=[]
        while start_number<=end_number:
            # print(start_number)
            if(start_number%7==0 and start_number%5==0):
                result.append(start_number)
            start_number+=1
        print(result)
    
    
    def func_conv_temp_cel_to_feh(temp_cel):
        result=(temp_cel*9/5)+32
        print(f"temprature from {temp_cel}' celcious to fehrenhite is : {result}")
        
        
    def func_draw_verticle_triangle(row_count):
        for i in range(0,row_count,1):
            for j in range(i):
                print("* ", end="")
            print("")
        for i in range (row_count,0,-1):
            for j in range(i):
                print("* ", end="")
            print("")

    def func_getFabonacci( end_num):
        x,y=0,1
        print(x , end=", ")
        while y<=end_num:
            print(y , end=", ")
            x, y = y, x+y 
        print("")
        
    def func_reverse_word(str_input):
        for i in range(len(str_input)-1,-1,-1):
            print(str_input[i] , end="")
        print("")

##find those numbers which are divisible by 7 and multiples of 5, 
# between 1500 and 2700 (both included). 
Operations.func_01(1500,2700)


##convert temperatures from Celsius to Fahrenheit.
##[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Operations.func_conv_temp_cel_to_feh(20)


## construct the following pattern, using a nested for loop.
'''
            * 
            * * 
            * * * 
            * * 
            *
'''
Operations.func_draw_verticle_triangle(5)


#accepts a word from the user and reverses it.
Operations.func_reverse_word("ajay")


##count the number of even and odd numbers in a series of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
print("count of even numbers is --> " , len(list(filter(lambda x:x%2==0,numbers))))
print("count of odd numbers is --> ", len(list(filter(lambda x:x%2!=0, numbers ))))



##get the Fibonacci series between 0 and 50. 
Operations.func_getFabonacci(8)