# 𝑓(𝑥)=𝑥**1/3 denkleminin kökünü bulmak için Newton raphson yöntemini kullanınız. 
# Elde edilen bulguları yorumlayınız

print("\nx(i+1)=x(i)-[f(x(i)/f'(x(i)))] olduğundan dolayi;\n")
print("x(i+1)=x-[(x**1/3)/1/3*(x**2/3)]\n")
print("x(i+1)=-2x(i)    elde edilir.\n")
print("Olusan denklemde kokun 0 olduğu acikca gorulmektedir.")
print("Ancak kok tahmini olarak 0'dan baska bir deger girildiginde iterasyonlarin sonucunda elde edecegimiz yeni koklerin yerel minimum noktasi etrafinda salinim yaptigini goruruz.")       
print("Gozlemlemek icin baslangic degeri olarak hem 0 hem de baska bir sayiyi giriniz ve cikan sonuclari inceleyiniz\n")

def NewthonRaphson(x):
    yeniKok=-2*x
    return yeniKok

for j in range(0,2):
    kok=int(input("Baslangic degeri olarak hangi sayiyi girmek istersiniz?:"))
    iterasyon=0
    for i in range(0, 4):
        iterasyon=iterasyon+1
        print(f"{iterasyon}. iterasyon \n    x={kok}")
        kok=NewthonRaphson(kok)
        print(f"    yeni_kok={kok}\n")
print("Elde ettigimiz bu sonuca gore Newthon-Raphson yöntemi bu denklemi cozmek icin uygun bir yontem degildir")