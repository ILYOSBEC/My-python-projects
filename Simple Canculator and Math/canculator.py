# canculator 

def canculator():


   while True:

    qiymat_1 = int(input("birinchi qiymatni kiriting >> "))
    amal = input(f"{qiymat_1} || endi esa amalni kiriting: (+,-,*,/) >> ")
    qiymat_2 = int(input(f"{qiymat_1} {amal}  || endi esa ikkinchi qiymatni kiriting >> "))
    print(f"{qiymat_1} {amal} {qiymat_2} = ? ")



    if amal == "+":
        javob = qiymat_1 + qiymat_2
    elif amal == "-":
        javob = qiymat_1 - qiymat_2 
    elif amal == "*":
        javob = qiymat_1 * qiymat_2 
    elif amal == "/":
        javob = qiymat_1 / qiymat_2 
    else:
       print("amalni to'gri kiriting !!!")
       continue    

    print(f"{qiymat_1} {amal} {qiymat_2} = {javob} ")


  
canculator()