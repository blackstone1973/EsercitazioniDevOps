num1=int(input("inserisci il primo numero  ")) # con cast a int
num2=int(input("inserisci il secondo numero  ")) # con cast a int
num3=int(input("inserisci il terzo numero  ")) # con cast a int

#ret = num1 + num2 + num3
# pass è come break;
if num1 > num2 and num1 > num3:
    print ("Il primo numero inserito è il più grande : " + str(num1))
elif num2 > num1 and num2 > num3:
    print ("Il secondo numero inserito è il più grande : " + str(num2))
elif num3 > num1 and num3 > num2:
    print ("Il terzo numero inserito è il più grande : " + str(num3))
else:
    print ("I numeri sono tutti uguali. "   + "Primo :" + str(num1) 
                                            + " Secondo :" + str(num1) 
                                            + " Terzo :" + str(num3))