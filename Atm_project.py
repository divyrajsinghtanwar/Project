Account_Holder={}

while True:
    name = input("enter name : ")
    if name == "":
        break
    balance = int(input(f"enter ${name}'s Current balance:"))
    pin  = int (input("enter pin : "))
  
    Account_Holder[name] ={
            "balance":balance,
            "pin" : pin
    }
    
print(Account_Holder)    


choiceofuser = ["Deposit","withdraw","check_balance","transaction_history","Exit"]

while True:
    user_name = input("enter account holder name for further services:")
    selectchioce = int(input("Enter choice from 1 -5:"))

    if selectchioce =="":
        break

    if selectchioce==1:
        newdeposit = int(input("enter deposit amount : "))
        Account_Holder[user_name]["balance"] +=newdeposit
        print(f"{newdeposit} is succsessfully deposited")

    elif selectchioce==2:
        newwithdraw = int(input("Enter withdrwal amount : "))
        Account_Holder[user_name]["balance"]-=newwithdraw
        print(f"{newwithdraw} successfully withdraw")

    elif selectchioce ==3:
        print("current balance :",Account_Holder[user_name]["balance"])

    elif selectchioce == 4:
        Transaction_history = {}
        print("Deposited :",newdeposit)
        print("withrawn : ",newwithdraw)
    else:
        print("Thank you for using Atm")
        break