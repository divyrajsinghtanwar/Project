Inventory_dict = {}

choice_list = ["Add_Product","Update_Quantity","Delete Product","ShowInventory","Most_Expensive_Product","Total_Inventory_Value","Exit"]
expensive_product=0
inventry_value =0
most_expensive = 0
total_inventry_value=0
while True:
    choice = int(input("enter choice : "))
    if choice =="":
        break

    if choice == 1:
        product =input("enter product name :")
        quantity = int(input("enter quantity : "))
        price = int(input("enter each price of product : "))
        Inventory_dict[product]={
            "quantity":quantity,
            "priceofproduct":price
        }
        print("product added successfully")
        inventry_value=quantity*price
        total_inventry_value+=inventry_value
        if most_expensive<price:
            most_expensive=price

    elif choice ==2 :
        input("enter product name :")
        newquantity = int(input("enter new quantity : "))
        Inventory_dict[product]["quantity"] = newquantity
        print("Quantity update sucessfully")

    elif choice ==3:
        delproduct =input("enter product name : ")
        del Inventory_dict[delproduct]
        print("proudct deleted successfully")    

    elif choice==4:
        print(Inventory_dict)

    elif choice ==5:
        print(f"most  expensive product : ",most_expensive)   

    elif choice ==6:
        print("total inventory value : $",total_inventry_value)
    else:
        print("Thank you")
        break