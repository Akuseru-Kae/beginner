#a python function that takes the limit as an argument of 
  the Fibonacci series and prints till that limit.

#fn is first number and sn is second number
nn is new number .




---------------
def fibonacci(num):
    fn=0
    sn=1
    print(fn,end=' ')
    print(sn,end=' ')
    for i in range(num):
        if fn+sn<=num:
            nn=fn+sn
            fn=sn
            sn=nn
            print(nn,end=' ')
fibonacci(10)
