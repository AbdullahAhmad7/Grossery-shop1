print("-------------------------"
      "Welcome to grossery shop"
      "-------------------------")
products={
          "Milk"    :  200,
          "Butter" : 100,
          }
print("select what you will buy if you don't want the specific one plz press enter")
print(products)
product1=input("what is your 1st product?").lower()
product2=input("what is your 2nd product?").lower()
# product3=input("what is your 3rd product?")

list={}
quantity={}

if product1=="butter":
    list["item_1"]="Butter"
    print(list)
    quantity=["item_1"]=int(input("enter quantity here?"))
if product1=="milk":
    list["item_1"]="Milk"
    quantity=["item_1"]=int(input("enter quantity here?"))
else:
    print("thanks")



if product2=="milk":
    list["item_2"]="Milk"
    print(list)
    quantity=["item_2"]=int(input("enter quantity here?"))  
if product2=="butter":
    list["item_2"]="Butter"
    print(list)
    quantity=["item_2"]=int(input("enter quantity here?"))
else:
    print("thanks")




Total_price=0
for item in list.values():
    Total_price+=products[item]*quantity
    print(Total_price)




