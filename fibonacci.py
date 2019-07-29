def fibonacci(n):
    if n<= 0:
        print("Invalid input.")
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) +fibonacci(n-2)
    
def main():
    n = int(input("Enter a positive integer: "))
    for n in range(1,n):
        print(fibonacci(n))
       
    
main()
    
    #add the last two numbers in a sequence together
    #print the result
