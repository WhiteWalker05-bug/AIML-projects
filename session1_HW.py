""" Name : Aditya Mhaskar 
    cohort:AI&ML - TEP cohort 2026
    Day: Monday
    date: 10/8/2026
    Description: this file contains the topics indexing,slicing and if and else statements, data type conversion and for loop and while loop examples  
"""

x=[10, "Hello", 3.14, True, None, 25, "Python", False]
print(x[5])

y="then you will be left in the dust, unless i stuck by ya"
print(y[0:6])

change=(23)
change_datatype=float(change)
print(type(change_datatype))

list=[]

for i in range(16):
    list.append(i)
    
print(list)    

i=0
while i<4:
    print(i)
    i+=1

person = {
    'first_name':'Aditya',
    'last_name':'Mhaskar',
    'age':250,
    'country':'westros',
    'is white walker':True,
    
    }
print(person['country']) # 7

verification=input("Are you a white walker?\n")
if verification=="yes":
    print("attack westros")
else:
    print("warn that winter is coming")    

