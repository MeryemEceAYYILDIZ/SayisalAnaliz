def faktoriyelAlma(adim):
    faktoriyel=1
    for i in range(1, adim+1):
        faktoriyel= faktoriyel* i
    return faktoriyel

def usAlma(sayi, adimsayisi):
    us=1
    for i in range(0, adimsayisi):
        us = us * sayi
    return us

gercekDeger=0.80901699437
pi=3.14
x=pi/5
adimsayisi=1
i=0
j=0
hesaplananDeger=0
while adimsayisi<=2:
    while i <= adimsayisi:
        if(i%2==0):
            hesaplananDeger = hesaplananDeger + usAlma(x, j)/faktoriyelAlma(j)
        else:
            hesaplananDeger = hesaplananDeger - usAlma(x, j)/faktoriyelAlma(j)
        i=i+1
        j=j+2
        kesmeHatasi=gercekDeger-hesaplananDeger
    print(f"{adimsayisi}. mertebedeki;\n hesaplanan deger: {hesaplananDeger} \n kesme hatasi: {kesmeHatasi}")
    adimsayisi=adimsayisi+1