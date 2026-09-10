#functions:
#1. built in
# 2. user defined

# def cal_prod(a,b):
#     print(a*b)
#     return a*b
# cal_prod(1,3)    


# def cal_prod(a=1,b=2):
#     print(a*b)
#     return a*b
# cal_prod(1)


#non default arguments are followed by default.

#WAP to print the length of a list.(list is the parameter).
# cities=["peshawar", "Islamabad", "Delhi"]
# cities2=["karachi", "Malakand", "Sialkot"]
# def print_len(list):
#     print(len(list))
#     return list

# print_len(cities2)
# print(cities2)

# print_len(cities)
# print(cities)

#WAF to print the elements of a list in a sigle line.(list id the parameter).
# cities3=["sawabi", "swat", "Mardan"]
# cities4=["multan", "etc"]

# def print_list(list):
#     for item in list:
#         print(item, end=" " )

# print_list(cities3)
# print()


#WAF to find tha factorial of n. (n is the parameter).
# 4!=1*2*3*4
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)


# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# cal_fact(5)


#wAF to convert USD to INR:

# def converter(usd_val):
#     inr_val = usd_val*83
#     print(usd_val, "usd =",inr_val, "INR")

# converter(100)

#WAF in which if the number is odd it will retuen odd and in even condition it will retuen even.

#Recursion:
#when a functin calls itself.

# def show(n):
#     print(n)
# show(5) # 5, 4, 3, 2, 1

# def show(n):
#     if(n==0):
#         return #base case is the stoping conditional.       
#     print(n)
#     show(n-1)
#     # print("end")
# show(5)
#call stack.

# def show(n):
#     # if(n==0):
#     #     return #base case is the stoping conditional.       
#     print(n)
#     show(n-1)
#     # print("end")
# show(5)

# def fac(n):
#     if(n==0 or n==1): #here we have taken 0 and 1 because 0 and 1 have same factorial.
#         return 1
#     else:
#         return fac(n-1)*n

# print(fac(1))

#write a recursion function to calculate the sum of first n natural numbers.
def cal_sum(n):
    if(n==0 ):
        return 0
    else:
        return cal_sum(n-1)+n #means that sum of n-1(4) in case of 5 is calculated and then 5(n) will be added to it.

sum=cal_sum(5)
print(sum)

























