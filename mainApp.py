import os # EKLEMEYİ UNUTMAYIN
import time  # BUNUDA UNUTMAYIN EĞER EKLEMEZSENİZ time.sleep(1) vs çalışmaz

# FONKSİYONLAR BAŞLANGIÇ

def çıkış():
	quit()

def user_read():
    with open("userinfo.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(user_giris())

def read():
    dosya = open("C:/--/--/Desktop/KayıtPythonGitHub/userinfo.txt", "r",encoding="utf-8")
    print(dosya.read())



def user_giris():
    ad = input("\nKullanıcı Adı : ")
    soyad = input("\nKullanıcı Soyadı : ")
    dogum_tarihi = input("\nDoğum Tarihi > Örnek(01-01-2020): ")
    okul_durumu = input("\nOkul Durumu > Örnek(Lise,Ortaokul,Üniversite) : ")
    telefon_no = input("\nTelefon Numarası > Örnek (****-***-**-**) : ")

    with open("userinfo.txt","a", encoding="utf-8") as file:
        file.write(ad+' '+ soyad+ ':'+dogum_tarihi+','+okul_durumu+','+telefon_no+'\n')

def user_kayitet():
    with open('userinfo.txt',"r",encoding="utf-8") as file:
        liste = []

# FONKSİYONLAR BİTİŞ 


# WHİLE DÖNGÜSÜ VE KODLAR

while True:
    # PROGRAMIİLK YAPTIĞIMDA BU SİSTEMİ KULLANMIŞTIM AMA ŞUAN DAHA GÜZEL GÖZÜKMESİ İÇİN KALDIRICAM SİZ İSTERSENİZ
    # TEKRARDAN ESKİ HALİNE GETİREBİLİRSİNİZ:

    print("""

            /1 Kullanıcıları Oku
            /2 Kullanıcı Kayıt Et
            /x Kullanıcıları Kayıt Et
            /q Çıkış --

        """)

    # ESKİ ANA EKRAN SİZ # LERİ KALDIRIP BUNLARI KULLANABİLİRSİNİZ
    #print(" --  1 Kullanıcıları Oku -- ")
    #print(" --  2 Kullanıcı Kayıt Et -- ")
    #print(" --  3 Kullanıcıları Kayıt Et -- ")
    #print(" --  4 Çıkış -- ")
 
    i = input("\nİşlem Seçmelisin ______ > ")
 
    if i == "1":
        read()
        print("\n^^^^^^^^^^^^^^^^")
 
    elif i == "2":
        user_giris()
        time.sleep(2)
        print("\nTebrikler Kullanıcı Başarılı Bir Şekilde Eklendi")
 
    elif i == "x" or i == "X":
        user_kayitet()
        print("\nKayıt Ediliyor Lütfen Bekleyiniz")
        time.sleep(4)
        print("\nBaşarıyla Kayıt Edildi")
 
    elif i == "q" or i == "Q":
        çıkıs()
        time.sleep(2)
        print("\nÇıkış Yapılıyor...")
    else:
        print("\nGeçersiz Giriş : ")
        time.sleep(1)
        input = ("\nAna Menüye Dönmek İçin Enter'e Bas : ")

# KODUN SONU