#hesap makinesi
while True:
    try:
        girilen_sayi1=int(input("bir sayi giriniz: "))
        girilen_sayi2=int(input("bir sayi giriniz: "))
    except ZeroDivisionError:
        print("bolen sifir olamaz")
    except ValueError:
        print("girdiginiz deger sayi olmalidir gecersiz bir deger girdiniz")
    else:
        break

a="+"
b="-"
c="*"
d="/"
islem_turu=input("bir islem turu seciniz (a=+, b=-,c=*,d=/): ")

if (islem_turu =="a"):
    sonuc=girilen_sayi1 + girilen_sayi2
    print(sonuc)
elif (islem_turu =="b"):
    sonuc=girilen_sayi1 - girilen_sayi2
    print(sonuc)
elif (islem_turu =="c"):
    sonuc=girilen_sayi1 * girilen_sayi2
    print(sonuc)
elif (islem_turu =="d"):
    sonuc=girilen_sayi1 / girilen_sayi2
    print(sonuc)
else:
    print("gecersiz islem turu girdiniz")


#sayı tahmin uyguluması
import random
for i in range(1):
   gercek_sayi=random.randint(1,100) #ikisi de dahil 

deneme_sayisi=1
tahmin=int(input("1 ile 100 arasinda uretilen sayiyi tahmin ediniz: "))

while (tahmin!=gercek_sayi):
    
    if (tahmin>gercek_sayi):
        print("daha kucuk")
    elif (tahmin<gercek_sayi):
        print("daha buyuk")
    tahmin=int(input("uretilen sayiyi tahmin ediniz: "))
    deneme_sayisi +=1

print(f"{deneme_sayisi}. seferinizde tahmin ettiniz")

#alisveris sepeti

liste=["elma","muz","cikolata"]
sepet=[]
kulalnici_istegi=input('listeden urun seciniz liste=["elma","muz","cikolata"]: ')
while (kulalnici_istegi!= "bitti"):
    sepet.append(kulalnici_istegi)
    kulalnici_istegi=input('listeden urun seciniz liste=["elma","muz","cikolata"]: ')

print(sepet)





    
    
    
