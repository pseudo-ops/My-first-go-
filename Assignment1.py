# a= input("Please enter a variable: ")
# try:
#     b=int(a)
#     print ('Variable entered:',b)
#     print('Type of variable: ', type(b))
#     print('Square of variable:',b**2)
# except:
#     print('Type of variable: ', type(a))
#     print("Sorry the string type can't be squared!")
#     print("Please enter an integer if you want the square of the input :)")
#     pass
        





# def distance_from_zero(x):
#     if type(x)==int or type(x)==float:
#         if x<=0:
#             x=x*(-1)
#             print(x)    
#     else:
#         print('What?')
            
# distance_from_zero("-33.4")


# #a        
# import random
# a,b=1,0
# while a>b:    
#     a= random.randrange(0,101)
#     b= random.randrange(0,101)
# print('a=',a, ",Type of a:", type(a))
# print('b=',b, ",Type of b:", type(b))
# #b)
# print("a/b:", a/b,",Type:", type(a/b) )
# print("a*b:", a*b,",Type:", type(a*b) )
# print("a+b:", a+b,",Type:", type(a+b) )
# print("a-b:", a-b,",Type:", type(a-b) )
# #c
# lst=[]
# for i in range(1000):
#     a=random.uniform(100,7999)
#     lst.append(a)

# lst_min=min(lst)
# print("min number=",lst_min)
# lst_max=max(lst)
# print("max number=",lst_max)
# lst.sort()
# print(lst)
# sum_lst=sum(lst)
# print("sum of all numbers=",sum_lst)

# count=0
# for x in lst:
#     y=int(x)
#     # ignore odd entries:
#     if y % 2 == 1:
#         continue
#     print("x =",y)
#     count+=1
# print("Count of Even Numbers=", count)


# #a
# def fib(N):
#     lst=[0,1]
#     for i in range(N-2):
#         a= lst[i] + lst[i+1]
#         lst.append(a)
#     print(lst)
# #b
# def fib(N):
#     lst=[0,1]
#     for i in range(N-2):
#         a= lst[i] + lst[i+1]
#         lst.append(a)
#     print(lst)
#     a=""
#     if N<=10:
#         for i in lst:
#             x=str(i)
#             a+=x
#         print('('+a+')')    
# fib(10)
# #C
# def fib(N):
#     lst=[1,1]
#     for i in range(N-2):
#         a= lst[i] + lst[i+1]
#         lst.append(a)
#     print(lst)
#     for i in range(N):
#         a=lst[i]
#         b=lst[i-1]
#         print(b)
#         print(a/b)
# fib(20)
            
    
    
    
    
    