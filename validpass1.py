def validpass(Passwd):
    C_Spc=0;C_Nmb=0;C_Upp=0  
    if len(Passwd)  >= 8:
        for C in Passwd:      
            if ord(C) >=35 and ord(C)<=38 or C=="!" or C=="@":C_Spc+=1
            if ord(C) >=48 and ord(C)<=57:C_Nmb+=1
            if ord(C) >=65 and ord(C)<=90:C_Upp+=1
            if ord(C) >=91 and ord(C)<=96 or ord(C) >=123 and ord(C)<=126 or ord(C) >=39 and ord(C)<=47 or ord(C) >=58
            and ord(C)<=63 or ord(C) >=128 and ord(C)<=254: return  2          
        if C_Nmb==0 or C_Spc==0 or C_Upp==0: return  3  
    else: return 4
    return 1


print("Enter a password with 8 or more character, at least 1 uppcase, 1 number and 1 special character...")

Passwd=''
state=0

while state!=1:
    Passwd=input("Enter password: ")
    state= validpass(Passwd)
    if state==2:print("Error: Only Special character (!, @, #, $, "+chr(38)+ " and "+ chr(37)+")")
    if state==3:print("Error: At least 1 uppercase, 1 number and 1 special character")
    if state==4:print("Enter new password, must have at least 8 characters =_=!")

print("Password accepted!***", )
 


       





 


