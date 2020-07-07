from os import system, name
def validpass(Passwd):
    Charz=""
    specialchars="@#$!%&"
    specialchars_denied="~`^*()_+|}{[]\=-':;/>.<,?"
    if len(Passwd)  >= 8 and len(Passwd) <= 16:
        if not any(Charz.isdigit() for Charz in Passwd): return 2
        if not any(Charz.isupper() for Charz in Passwd): return 3
        if not any(Charz.islower() for Charz in Passwd): return 4
        if not any(Charz in specialchars for Charz in Passwd): return 5   
        if  any(Charz in specialchars_denied for Charz in Passwd): return 6   
        
    elif len(Passwd) < 8 or len(Passwd) > 16: return 7
    return 1

_ = system('cls')
print("Enter a password with 8 or more character, at least 1 uppcase, 1 number and 1 special character...")
Passwd=''
state=0
while state!=1:
    Passwd=input("Enter password: ")
    state= validpass(Passwd)
    if state==2:print("Error: At least one number 0 - 9")
    if state==3:print("Error: At least 1 uppercase")
    if state==4:print("Error: At least 1 lowercase")
    if state==5:print("Error: At least 1 Special character:@#$!%&")
    if state==6:print("Error: Only special characters is allowed: @#$!%&")
    if state==7:print("Error: No less than 8 characters or more than 16 characters")
    
print("Valid Password!!!!!***")
 


       





 


