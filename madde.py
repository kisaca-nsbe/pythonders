while(True):
    sicaklikDegeri=int(input('Sicaklik Degerini Giriniz:'))
    if(sicaklikDegeri<0):
        print('ürün katıdır')
    elif(sicaklikDegeri>0 and sicaklikDegeri<=100):
        print('ürün sıvıdır')
    else:
        print('ürün gazdır')
