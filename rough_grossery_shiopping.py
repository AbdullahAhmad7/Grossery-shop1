print("-------------------------"
      "Welcome to grossery shop"
      "-------------------------")
products={
          "Milk"    :  200,
          "Butter" : 100,
          }


print(products)
cart={}
quantity={}
counter=1
Total_price=0

for item in products:
    item_1=input("Enter your product?").lower()
    item_1=item_1.capitalize()
    if item_1 in products:
        cart[f"item_{counter}"]=item_1
        quantity[f"item_{counter}"]=int(input("Enter quantity here {item_1}= "))
        counter+=1
print(cart)

for key in cart:
    product_name=cart[key]
    price=products[product_name]
    qty=quantity[key]
    Total_price += price *qty
print("your Total price is ",Total_price)

if Total_price>=1000:
    print("you have got discount")
else:
    print("Thanks!")

Total_price_with_discount=Total_price*0.9
print("Your final discounted price is ",Total_price_with_discount)


print("Here are your products=",cart)




