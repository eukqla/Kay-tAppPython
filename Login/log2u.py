import time
import os


def çıkış():
    quit()

print("""

                E = LOGIN
                H = SIGN UP

                Q- Exit

            """)

welcome = input("\n Lütfen İşlem Seçiniz.")
print("\n Bu İşlem Uzun Sürebilir Lütfen Programı Kapatmayınız")
time.sleep(6)




if welcome == "H" or welcome == "h":

    while True:
        username  = input("\n Kullanıcı Adı Giriniz :")
        password  = input("\n Şifre Giriniz : ")
        password1 = input("\n Şifre Doğrulayın : ")
        time.sleep(2)
        print("\n Loading......")
        #print("\n .............")

        if password == password1:
            file = open(username+".txt", "w")
            file.write(username+":"+password)
            file.close()
            welcome = "e"
            break
            print(".......")
            time.sleep(1)
            print("Uygunluk Kontrol Ediliyor")
            time.sleep(3)
        print("\n Şifre Eşleşmiyor TEKRAR Deneyiniz!")

 
if welcome == "E" or welcome == "e":

    while True:
        login1 = input("\n Kullanıcı Adı ------->> ")
        login2 = input("\n Şifre ------->> ")
        file = open(login1+".txt", "r")
        data   = file.readline()
        file.close()
        if data == login1+":"+login2:
            print("\n Kısa Bir Süre Bekleticeğiz.....")
            time.sleep(5)
            print("\n Sabrın İçin Teşekkür Ederiz")
            time.sleep(3)
            print("\n Giriş Yapılıyor......")
            time.sleep(4)
            os.startfile("C:/--/--/Desktop/--/mainApp.py")
            time.sleep(0.8)
            quit()
            break
        print("\n Şifre Veya Parola Eşleşmiyor,Lütfen Düzgün Yazdığınızdan Emin Olunuz.")


if welcome == "Q" or welcome == "q":
    print("\n Çıkış Yapılıyor...")
    time.sleep(3)
    çıkış()