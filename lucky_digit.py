'''algorithm:
    find digits of given number until n is zero
    if
        if sum is not yet a single digit number then repeat step one
    else
        print the sum as output
    input_num= 789
    input_num= 789//10 #78
    remainder=789%10 #9 

'''

input_num=int(input('Enter a number to find your lucky digit:'))
print(f'Number you input is {input_num}')
def adder(input_num):
    while True:
        sum_of_digits=0
        remainder=input_num%10
        input_num=input_num//10
        sum_of_digits+=remainder
        if sum_of_digits>9 and input_num==0:
            return adder(sum_of_digits)
        
    
            return sum_of_digits
            

print(f'Lucky number is',adder(input_num))



