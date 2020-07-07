
Charz=""
SpChars="@!%&#$"
SpChars_denied="~`()_+=-{[}]\|;:?/>.<,/?"
errx=[]
Passwd=""

while Passwd!=1:
    Passwd=input("enter password :")
    if len(Passwd)>=8 and len(Passwd)<=16:
        if not any(Charz.isdigit() for Charz in Passwd): errx+=["At least one Number"]
        if not any(Charz.isupper() for Charz in Passwd): errx+=["At least one Upper case"]
        if not any(Charz.islower() for Charz in Passwd):errx+=["At least one Lower case"]
        if any(Charz in SpChars_denied for Charz in Passwd):errx +=["Special chars only: "+SpChars]
        if not any(Charz in SpChars for Charz in Passwd):errx+=["At least one Special char"]
        
    elif len(Passwd) <8 or len(Passwd)> 16: errx+=["Must be at least 8 Characters"]
    
    if len(errx)> 0:
        for x in range(len(errx)):
            print("**** "+errx[x])
        errx=[]
    else: print("Password accepted")
     