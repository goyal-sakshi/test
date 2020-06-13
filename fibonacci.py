
# 0 1 1 2 3 5 8 
# 5 - >  0 1 1 2 3

def fib(n):
   ll = [0,1]
   for i in range(2,n):
       ll.append(ll[i-2] + ll[i-1])
   print(ll)

#def fib(n):
#    if n== 0 or n==1:
#        print(n)
#    a,b = 0, 1
#    print(a, b)
#    for _  in range(2, n):
#        a,b = b , a+b
#        print(b)

# fib(5)
fib(1)


