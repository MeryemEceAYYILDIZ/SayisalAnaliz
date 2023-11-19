#𝑥3+4𝑥2−10=0denkleminin 1 2 aralığında kökünü ikiye
#bölme metodu ile 4 iterasyonda gerçekleştiriniz Bulunan çözümün
#kodunu hazır fonksiyon kullanmadan yazınız Çözüme

def yeniKok(x_alt, x_ust):
    x_kok=(x_alt+x_ust)/2
    return x_kok

def bisection(iterasyon, x_alt, x_ust, x_kok):
    fx_alt=(x_alt**3)+(4*(x_alt**2))-10
    fx_ust=(x_ust**3)+(4*(x_ust**2))-10
    fx_kok=(x_kok**3)+(4*(x_kok**2))-10
    if((fx_alt*fx_kok)<0):
        if(fx_alt<fx_kok):
            yeni=yeniKok(x_alt, x_kok)
            alt=x_alt
            ust=x_kok
        else:
            yeni=yeniKok(x_kok, x_alt)
            alt=x_kok
            ust=x_alt

    elif((fx_ust*fx_kok)<0):
        if(fx_ust<fx_kok):
            yeni=yeniKok(x_ust, x_kok)
            alt=x_ust
            ust=x_kok
        else:
            yeni=yeniKok(x_kok, x_ust)
            alt=x_kok
            ust=x_ust
    iterasyon=iterasyon+1
    print(f"{iterasyon}. iterasyon \nf({x_alt})={fx_alt} \nf({x_ust})={fx_ust} \nf({x_kok})={fx_kok} \n")
    return iterasyon, alt, ust, yeni

i, a, u, y = bisection(0, 1, 2, 1.5)
i, a, u, y = bisection(i, a, u, y)
i, a, u, y = bisection(i, a, u, y)
i, a, u, y = bisection(i, a, u, y)