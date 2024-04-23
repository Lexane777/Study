listArmstrong=[]
listNumber=[0,1,2,3,4,5,6,7,8,9]
for Num1 in listNumber:
    for Num2 in listNumber:
        for Num3 in listNumber:
            if (((Num1**3)%10+(Num2**3)%10+(Num3**3)%10)%10==Num1):
                result1=int(str(Num3)+str(Num2)+str(Num1))
                result2=int(str(Num2)+str(Num3)+str(Num1))
                if(result1==Num1**3+Num2**3+Num3**3 and result1>100):
                    #print("Число Армстронга: "+str(result1))
                    listArmstrong.append(result1)

                elif (result2==Num1 ** 3+Num2 ** 3+Num3**3 and result2>100):
                    #print("Число Армстронга: " + str(result2))
                    listArmstrong.append(result2)
print("Числа Армстронга:"+str(set(listArmstrong)))



