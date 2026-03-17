# bu dastur misol beruvchi dastur

import random

def misol_beruvchi(x=100, y=100):
    misol_son = 0
    togri = 0
    xato = 0

    while True:
        random_son_01 = random.randint(1, x)
        random_son_02 = random.randint(1, y)
        amal = random.choice(['+', '-', '*', '/'])


        if random_son_01 % 2 != 0:
            random_son_01 += 1
        if random_son_02 % 2 != 0:
            random_son_02 += 1


        if amal == "/" and random_son_02 == 0:
            random_son_02 = 1

        print("\nMen sizga (+, -, *, /) amallar orqali random tarzda misol beraman:")

        if amal in ["-", "/"] and random_son_01 < random_son_02:
            a, b = random_son_02, random_son_01
        else:
            a, b = random_son_01, random_son_02

        print(f"{a} {amal} {b} = ?")



        try:
            yechish = float(input(">>> "))
        except ValueError:
            print("Iltimos, faqat son kiriting!")
            continue


        if amal == "+":
            savol = a + b
        elif amal == "-":
            savol = a - b
        elif amal == "*":
            savol = a * b
        elif amal == "/":
            savol = round(a / b, 2)

        # Javobni tekshirish
        misol_son += 1
        if yechish == savol:
            togri += 1
            print("✅ Tabriklayman 🎉 Siz to'g'ri topdingiz!")
        else:
            xato += 1
            print(f"❌ Xato! To‘g‘ri javob {savol} edi.")

        # Davom ettirish yoki to‘xtatish
        yana_play = input("Yana o‘ynaysizmi (ha/yoq): ").lower()
        if yana_play == "yoq":
            print("\n📊 O‘yinning yakuni:")
            print(f"Jami misollar: {misol_son}")
            print(f"✅ To‘g‘ri javoblar: {togri}")
            print(f"❌ Xato javoblar: {xato}")
            break

misol_beruvchi()
