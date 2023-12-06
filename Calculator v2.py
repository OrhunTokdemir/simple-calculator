print("Hesap makinesine hoşgeldiniz.")
while True:
    try:
    #ilk girilen sayı arg0. eğer girilen değer bir sayı değilse hata mesajı verir ve tekrar sayı ister.
        arg0 = float(input("Başlangıç sayısı giriniz:"))
        break
    except:
        print("Hatalı sayı girdiniz. Lütfen tekrar sayı giriniz.")
while True:
    #tanımlanan dört işlemden birini seçer eğer tanımsız bir değer girilirse hata verip tekrar değer ister.
        islem = str(input("Toplama için: +, Çıkarma için: -, Çarpma için: *, Bölme için: / işaretini giriniz:"))
        if islem=="+" or islem=="-"or islem== "*" or islem== "/" :
            break
        else:
            print("Hatalı işlem girdiniz. Lütfen tekrar işlem giriniz.")
            continue
def dort_islem(x,z):
    #hesap makinesinin dört işlem özelliğinin tamamı tek bir fonksiyon altında.
    #hesap makinesi her bir işlemin sonunda yeni sayı değeri ve işlem değeri alırken doğru girilmişmi diye kontrol eder ve ona göre ya hata verir yada işleme devam eder.
    while True:
        if z=="+":
            while True:
                #Toplama
                if z=="+":
                    while True:
                        try:
                            y = float(input("yeni sayı giriniz:"))
                            break
                        except:
                            print("Hatalı sayı girdiniz. Lütfen tekrar sayı giriniz.")

                    x +=  y
                    print("Sonuç= ",x)
                    z = str(input("Toplama için: +, Çıkarma için: -, Çarpma için: *, Bölme için: / işaretini giriniz.\nVeya son işlemi tekrar etmek için enter'a basın." ))
                elif z=="":
                    x+= y
                    print("Sonuç= ",x)
                    z = str(input("Toplama için: +, Çıkarma için: -, Çarpma için: *, Bölme için: / işaretini giriniz.\nVeya son işlemi tekrar etmek için enter'a basın." ))
                else:
                    break
        elif z=="-":
            while True:
                #Çıkarma
                if z=="-":
                    while True:
                        try:
                            y = float(input("yeni sayı giriniz:"))
                            break
                        except:
                            print("Hatalı sayı girdiniz. Lütfen tekrar sayı giriniz.")

                    x-=y
                    print("Sonuç= ",x)
                    z = str(input("Toplama için: +, Çıkarma için: -, Çarpma için: *, Bölme için: / işaretini giriniz.\nVeya son işlemi tekrar etmek için enter'a basın." ))
                elif z == "":
                    x -= y
                    print("Sonuç=",x)
                    z = str(input(
                        "Toplama için: +, Çıkarma için: -, Çarpma için: *, Bölme için: / işaretini giriniz.\nVeya son işlemi tekrar etmek için enter'a basın."))

                else:
                    break
        elif z=="*":
            while True:
                if z=="*":
                    #Çarpma
                    while True:
                        try:
                            y = float(input("yeni sayı giriniz:"))
                            break
                        except:
                            print("Hatalı sayı girdiniz. Lütfen tekrar sayı giriniz.")

                    x *= y
                    print("Sonuç= ",x)
                    z = str(input("Toplama için: +, Çıkarma için: -, Çarpma için: *, Bölme için: / işaretini giriniz.\nVeya son işlemi tekrar etmek için enter'a basın." ))
                elif z == "":
                    x *= y
                    print("Sonuç= ",x)
                    z = str(input(
                        "Toplama için: +, Çıkarma için: -, Çarpma için: *, Bölme için: / işaretini giriniz.\nVeya son işlemi tekrar etmek için enter'a basın."))

                else:
                    break
        elif z=="/":
            while True:
                if z=="/":
                    while True:
                        #Bölme
                        try:
                            y = float(input("yeni sayı giriniz:"))
                            break
                        except:
                            print("Hatalı sayı girdiniz. Lütfen tekrar sayı giriniz.")
                    x /= y
                    print("Sonuç= ",x)
                    z = str(input("Toplama için: +, Çıkarma için: -, Çarpma için: *, Bölme için: / işaretini giriniz.\nVeya son işlemi tekrar etmek için enter'a basın." ))
                elif z == "":
                    x /= y
                    print("Sonuç= ",x)
                    z = str(input("Toplama için: +, Çıkarma için: -, Çarpma için: *, Bölme için: / işaretini giriniz.\nVeya son işlemi tekrar etmek için enter'a basın."))
                else:
                    break
        elif z=="kill":
            #uygulamayı sonlandırır.
            break
        else:
            while True:
                if z == "+" or z == "-" or z == "*" or z == "/":
                    break
                else:
                    print("Hatalı işlem girdiniz. Lütfen tekrar işlem giriniz.")
                    z = str(input("islem:"))
                    continue

dort_islem(arg0,islem)
