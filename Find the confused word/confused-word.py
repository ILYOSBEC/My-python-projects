# bir sozni harflar joyini ozgartirib beradi va siz uni topishingiz kerak
import random
from uzwords import words


def confused_word():
    word = random.choice(list(words))
    while "-" in word or " " in word:
        word = random.choice(list(words))
    return word.upper()


def give_word():
    question = 0
    true_word = 0
    false_word = 0

    while True:
        word = confused_word()

        # So'z harflarini aralashtirish
        harflar = list(word)
        random.shuffle(harflar)
        shuffled_word = "".join(harflar)

        print("\nMen harflari aralashgan so'z beraman, siz uni to'g'risini yozing!")
        print(f"Aralashgan so'z: {shuffled_word}")

        answer = input("Javobni kiriting: ").upper()

        question += 1
        
        if answer == word:
            true_word += 1
            print("🎉 To'gri topdingiz!")
        else:
            false_word += 1
            print(f"❌ Noto'g'ri! To'gri javob: {word}")

        yana = input("\nYana o'ynaysizmi? (ha/yoq): ").lower()
        if yana == "yoq":
            break

    print("\n📊 O'yin yakunlandi:")
    print(f"Jami savollar: {question}")
    print(f"✅ To'g'ri javoblar: {true_word}")
    print(f"❌ Xato javoblar: {false_word}")


give_word()






