#kullanıcıdan veri alınıp listeye eklenme örnekleri


print('Hoşgeldiniz! Çıkmak için Q basınız')

liste=[]
isimSoyisim=str(input('isim Soyisim:'))
TcNo=str(input('Tc No:'))
yasadiginizIl=str(input('Yaşadığınız İl:'))


liste.append(isimSoyisim)
liste.append(TcNo)
liste.append(yasadiginizIl)
print(liste)
