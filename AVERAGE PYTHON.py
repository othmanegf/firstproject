n1=float(input("enter the 1st note: "))
n2=float(input("enter the 2nd note: "))
n3=float(input("enter the 3rd note: "))  
while n1>20 or n1<0 :
    n1=float(input("please enter the 1st note between 0 and 20: "))                        
while n2>20 or n2<0 :
    n2=float(input("please enter the 2nd note between 0 and 20: "))
while n3>20 or n3<0 :
    n3=float(input("please enter the 3rd note between 0 and 20: "))
average=(n1+n2+n3)/3                    
if average >= 16:
    mention = "Very good"
elif 14 <= average < 16:
    mention = "Good"
elif 12 <= average < 14:
    mention = "Fairly good"
elif 10 <= average < 12:
    mention = "Passable"
else:
    mention = "Insufficient"

# the average and mention":        
print ("The average is :", average,"and the mention is", mention)