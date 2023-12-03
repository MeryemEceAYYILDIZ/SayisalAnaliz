#Kullanıcıdan bir sayı alın ve bu sayının faktöriyelini hesaplayın. 
sayi=int(input("Hangi sayinin faktoriyelini almak istiyorsunuz?:"))
faktoriyel=1
for i in range(1, sayi+1):
    faktoriyel= faktoriyel* i
print(faktoriyel)

#Kullanıcıdan alınan iki sayının en büyük ortak bölenini hesaplayın.
sayi1=int(input("1. sayiyi giriniz:"))
sayi2=int(input("2. Sayiyi giriniz:"))
if(sayi1>sayi2):
     kucukSayi=sayi2
else:
     kucukSayi=sayi1
for i in range(1,kucukSayi+1):
     if(sayi1%i==0) and (sayi2%i==0):
        ebob=i
print("Girilen sayilarin ebobu:", ebob)

#Kullanıcıdan alınan sayının asal olup olmadığını kontrol eden python kodunu yazınız.
sayi3=int(input("Asal kontrol edeceğiniz sayiyi giriniz"))
sayac=0
for i in range(2,int((sayi3/2)+1)):
    if(sayi3%i==0):
        sayac=sayac+1
if (sayac!=0):
    print("Asal sayi degildir")
else:
    print("Asal sayidir")

#Kullanıcıdan alınan sayı kadar fibonacci serisi oluşturan python kodunu yazınız.
adim=int(input("Hangi adima kadar fibonacci yazdirmak istiyorsunuz?"))
guncelSayi=1
birOnce=1
ikiOnce=0
for i in range(1, adim+1):
	print(guncelSayi)
	guncelSayi=birOnce+ikiOnce
	ikiOnce=birOnce
	birOnce=guncelSayi
     
#Kullanıcıdan kelime veya cümle alın ve bu kelime veya cümlenin palindrom olup olmadığını kontrol edin
string=input("Bir kelime veya cumle giriniz:")
terStr=string[::-1]
if(string==terStr):
     print("Palindromdur")
else:
     print("Palindrom degildir")