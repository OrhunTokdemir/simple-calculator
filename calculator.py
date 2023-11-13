print("Hesap Makinesine Hoşgeldiniz")
print("Sayı değerlerinizi giriniz ardından işleminizi seçiniz")

arg1 = int(input("sayı1:"))
arg2 = int(input("sayı2:"))
cal = input("toplama için:+, çıkarma için:-, çarpma için:*, bölme için:/ değerini giriniz.")

toplam = lambda  arg1,arg2:arg1+arg2
cikarma = lambda  arg1,arg2:arg1-arg2
carpma = lambda arg1,arg2:arg1*arg2
bolme = lambda arg1,arg2:arg1/arg2
#kare = lambda arg1:arg1*arg1
#karekok = lambda arg1:math.sqrt(arg1)
while True:
    if cal == "+":
        print("sonuç=",toplam(arg1,arg2))
        break
    elif cal == "-":
        print("sonuç=",cikarma(arg1,arg2))
        break

    elif cal == "*":
        print("sonuç=",carpma(arg1,arg2))
        break
    elif cal == "/":
        print("sonuç=",bolme(arg1,arg2))
        break

    else:
        print("hatalı işlem girdiniz lütfen tekrar giriniz")
        cal = input("toplama için:+, çıkarma için:-, çarpma için:*, bölme için:/ değerini giriniz.")
        continue



