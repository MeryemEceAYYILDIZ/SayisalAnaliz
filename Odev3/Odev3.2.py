# 𝑓(𝑥)=4*(𝑒^(−0.5𝑥))−𝑥 denkleminin kökünü başlangıç değeri 𝑥0=2alarak 4 iterasyon sonucunda bulunuz 
# Bulunan çözümün kodunu hazır fonksiyon kullanmadan yazınız

#x(i+1)=x(i)-[f(x(i)/f'(x(i)))] olduğundan dolayı;
#x(i+1)=x(i)-[4*(𝑒^(−0.5*x(i)))−x(i)/-((2+e**(0,5*x(i)))/e**(0,5*x(i)))]
#x(i+1)=(2*x(i)+4)/(2+e**(0,5*x(i)))

def NewthonRaphson(x):
    e=2.71828182846
    yeniKok=(2*x+4)/(2+(e**(0.5*x)))
    return yeniKok

kok=2
iterasyon=0
for i in range(0, 4):
    iterasyon=iterasyon+1
    print(f"{iterasyon}. iterasyon \n    x={kok}")
    kok=NewthonRaphson(kok)
    print(f"    yeni_kok={kok}\n")
    

    