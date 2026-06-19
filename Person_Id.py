import csv
import pandas as pd

while True :
    first_Name = input("Enter First name : ")
    last_Name = input("Enter last name : ")
    Age = int(input("Enter your age : "))
    city = input("Enter city name : ")
    state = input("Enter state : ")
    Skill = input("Enter skill you Known : ")

    total_Name_count = len(first_Name)+len(last_Name)
    total_City_count = len(city)+len(state)
    total_skill_count = len(Skill)

    print("-"*41)
    print("|   Name :",first_Name,"",last_Name," "*(25-total_Name_count),"|")
    print("|   Age  :",Age,"Years" +" "*21 + "|")
    print("|   City :"+city+", "+state+" "*(28-total_City_count)+"|")
    print("|   Skill:"+Skill+" "*(30-total_skill_count)+"|")
    print("-"*41)


    record = {
        'Name':[first_Name+last_Name],
        'Age':[Age],
        'city' :[city],
        'state':[state],
        'skill':[Skill],
    }

    df = pd.DataFrame(record)
    df.to_csv('record.csv',mode='a',index=False)

    with open('record.csv','a',newline='') as f :
        csv.writer(f).writer.writerows([first_Name + ""+last_Name,Age,city,state,Skill])

    newstudent = input("you want to other person (Y/N) :")
    if newstudent == "N":
        break
