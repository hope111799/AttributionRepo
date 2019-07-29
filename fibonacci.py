# -------------------------------------------------
#        Name: <VIC BROWN and HERMILLA FENTAW>
#    Filename: repolab.py
#        Date: <July 29, 2019>
#
# Description: < Learning how to use github and terminal>
# -------------------------------------------------

def fibonacci(n):
    if n<= 0:
        print("Invalid input.")
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) +fibonacci(n-2)
    
def main():
    n = int(input("Enter a positive integer: "))
    for n in range(1,n):
        print(fibonacci(n))
       
    
main()
## -------------------------------------------------
## Code created with the help of xanasa14
##
## 
##fibonacci_cache  = {}
##def fibonacci (n):
##    if n in fibonacci_cache:
##        return fibonacci_cache[n]
##    if n == 1:
##        value = 1
##    elif n == 2:
##        value = 1
##    elif n > 2:
##        value = fibonacci(n-1) + fibonacci(n-2)
##    fibonacci_cache[n] = value
##    return value
##for n in range(1, 10):
##    print (n," times in fibonacci is " , fibonacci(n))
## -------------------------------------------------

    
    #add the last two numbers in a sequence together
    #print the result


