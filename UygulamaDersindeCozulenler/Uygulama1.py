#Merhaba dünya stringini bir değişkene atayın ve ekrana yazdırın
cumle = "Merhaba, Dünya"
print(cumle)
#   Yazdırdığınız değerin içerisindeki b harfinin konumunu bulun

#   yukarıdaki stringin bütün harflerini büyük ve küçük olarak ekrana yazdırın
buyuk = cumle.upper()
kucuk = cumle.lower()
print(f"Hepsi buyuk: {buyuk}\nHepsi kucuk: {kucuk}")

#   yukarıdaki string içerisinde istediğiniz bir kullanarak bunu parçalayın
cumle = cumle.split("a")
print(cumle)

# İki değişken tanımlayın ve bunlara birer değer atayarak boolean operatörü ile karşılaştırma yapın. 
# (Sonuçlar (True, False) olmalıdır)
x=5
y=4
print(bool (x<y))

Liste = [1, "a", 2, 3, True, 4, 5, "True", "1"]
# Verilen listeyi kullanarak aşağıdaki şıkları yanıtlayın
#   Listenin son elemanını bulun
print(Liste[-1])

#   yeni bir liste oluşturun ve yukarıdaki listenin ikinci ve üçüncü elemanlarını içerisine atayın
newListe=Liste[2:4]
print(newListe)

#   Listeyi ters sıralayın
print(Liste[::-1]) #Bu soruda reverse de kullanılabilir

ic_ice_liste = [1,2,3,[4,5]]
# Listeyi kullanarak aşağıdaki soruları yanıtlayın
# Listedeki 5 değerini ekrana yazdırın
print(ic_ice_liste[3][1])

# Listenin son elemanını listeden atın ve yerine yeni bir eleman ekleyin
ic_ice_liste.pop()
ic_ice_liste.append(7)
print(ic_ice_liste)

ic_ice_liste = [1,2,3,[4,5]]
# Pop komutunu kullanmayarak listede bulunan "3" karakterini silin (1,2[4,5] çıktı sonucu olacaktır)
del ic_ice_liste[2] # Bu soruda split ile 3'ü ayıraç olarak kullanıp ayırabilirsin,
                    # daha sonra tekrar oluşan diziyi tekrar birleştirebilirsin
print(ic_ice_liste)

my_dict = {
            "isim": "Mesut",
            "yas": 32,
            "lokasyon": {
                "yasadiği": "Berlin",
                "dogdugu": "Istanbul",
            }
        }
# Yukarıdaki dictionaryi kullanarak aşağıdaki soruları cevaplayınız
#   32 değerine ulaşıp ekrana yazdırınız
print(my_dict["yas"])

#   isim anahtarına denk gelen değeri kendi isminizle değiştirin
my_dict["isim"]="Meryem Ece"
print(my_dict["isim"])

#   İstanbul değerine ulaşıp ekrana yazdırın
print(my_dict["lokasyon"]["dogdugu"])
#    Bütün anahtar değerlerine ulaşıp ekrana yazdırınız
print(my_dict)