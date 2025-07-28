import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

print("-----c-----")
mydata=pd.read_csv("data.csv")
#Display Top 3 Rows of The Dataset
print("Top 3 Rows: ")
print(mydata.head(3).to_string())
print(" ")
#2)	Check Last 3 Rows of The Dataset
print("Bottom 3 Rows: ")
print(mydata.tail(3).to_string())
print(" ")
#3)Check null values in the dataset :
print("Total null value in each column: ")
print(mydata.isnull().sum())
print(" ")
#4)How many rows and columns are there in our Dataset?
print("Total columns and rows: ")
print("Columns :",len(mydata.columns))
print("Rows :",len(mydata))
print(" ")
#Highest and Lowest Purchase Prices?
print("Highest and Lowest Purchase Prices: ")
print("Higest: ",mydata["Purchase Price"].max())
print("Lowest: ",mydata["Purchase Price"].min())
print(" ")
#Average Purchase Price?
print("Average Purchase Price: ",mydata["Purchase Price"].mean())
print(" ")
#How many people have French 'fr' as their Language?
print("Total no of people learning French as their Language: ",len(mydata[mydata["Language"]=="fr"]))
print(" ")
#Job Title Contains Engineer?
print("Total no of people Job Title Contains Engineer: ",len(mydata[mydata["Job"]=="Engineer"]))
print(" ")
#Find The Email of the person with the following IP Address: 10.0.0.8?
print("Email of the person with the following IP Address: 10.0.0.8: ",mydata[mydata["IP Address"]=='10.0.0.8']["Email"])
print(" ")
#How many People have Mastercard as their Credit Card Provider and made a purchase below 70?
print("No of people have Mastercard as their Credit Card Provider and made a purchase below 70: ",len(mydata[(mydata["CC Provider"]=="MasterCard") & (mydata["Purchase Price"]<70)]))
print(" ")
#Find the email of the person with the following Credit Card Number: 6011000990139424
print("Email of the person with the following Credit Card Number (6011000990139424):",mydata[mydata["Credit Card"]==6011000990139424]["Email"])
print(" ")
#How many people purchase during the AM and how many people purchase during PM?
print("People puchase during ",mydata["AM or PM"].value_counts())
print(" ")
#How many people have a credit card that expires in 2025?
a=mydata["CC Exp Date"]
c=0
for i in a:
    b=(i.split("/"))
    if b[1]=='25':
        c+=1
print("People have a credit card that expires in 2025: ",c)
print(" ")
#What are the most popular email providers (e.g.   gmail.com, yahoo.com, etc
a=mydata["Email"]
b=[]
for i in a:
    if i.split("@")[1] not in b:
        b.append(i.split("@")[1])
print("Most popular email providers: ",b)
