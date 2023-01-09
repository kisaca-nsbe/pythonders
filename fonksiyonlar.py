def yasHesaplama(dogumYili):
    return 2023-dogumYili

def emeklilikYasi(dogumYili,isim):
    yaslar=yasHesaplama(dogumYili)
    emeklilik=65-yaslar
    if emeklilik>0:
        print(f"Emeklilik: {emeklilik} yıl kaldi...")
    else:
        print('Tebrikler')

emeklilikYasi(1991,'nazlı')



def kelimeYazdir(kelime, adet):
    print(kelime * adet)

kelimeYazdir('10',10)

def asalSayilariBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi>1:
            for i in range(2,sayi):
                if(sayi%i==0):
                    break
                else:
                    print(sayi)
sayi1=int(input('Sayı 1:'))
sayi2=int(input('Sayı 2:'))
asalSayilariBul(sayi1,sayi2)

def tamBolenler(sayi):
    tamBolenler=[]
    for i in range(2,sayi):
        if (sayi % i==0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenler(20))

def faktoriyel(sayi):
    if sayi==0:
        return 1
    else:
        return sayi * faktoriyel(sayi-1)
print(faktoriyel(5))


def kayitOlustur(isim,soyisim,tc,sehir):
    print('-'*30)
    print('isim        :  ',isim)
    print('soyisim     :  ',soyisim)
    print('tc          :  ',tc)
    print('sehir       :  ',sehir)
    print('-'*30)

kayitOlustur('Nazlı','Elmalı','123456789','İzmir')