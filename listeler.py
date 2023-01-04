ilk_liste=[10,20,30,40,50]
print(ilk_liste)
print('-----')
ikinci_liste=['Burak','Nazlı',24,12,2.16,True]
print(ikinci_liste)
print('-----') 
ucuncu_liste=['N','S','B','E']
for harfler in ucuncu_liste:
    print(harfler)
print('-----')
dorduncu_liste=['N','S','B','E',0.8,3]
print(dorduncu_liste[5])
print('-----')
besinci_liste=[5,10,12,13,14,19,20]
for i in besinci_liste:
    if i%2==0: #2ye kalansız bölüneni bul
        print(i)
print('-----')
altinci_liste=['N','A','Z','B','U','R']
print(altinci_liste[2:6]) #2-6 sıra arası (6 dahil değil) gösterir
print('-----')
altinci_liste=['N','A','Z','B','U','R'] #0'dan 3. elemana kadar gösterir 0,1,2
print(altinci_liste[:3])
print('-----')
yedinci_liste=['N','A','Z','L','I']
sekizinci_liste=['S','E','D','A']
yeni_liste=yedinci_liste + sekizinci_liste
print(yeni_liste)
print('-----')
dokuzuncu_liste=[1,2,3,4,5,6,7]
del dokuzuncu_liste[3] #3. elemanı sil
print(dokuzuncu_liste)
print('-----')
onuncu_liste=['N','A','Z','L','I']
adet=len(onuncu_liste)
print(adet)
print('-----')
onbirinci_liste=['N','A','Z','L','I',]
#test='Q' in onbirinci_liste
#print(test)
if 'A' in onbirinci_liste:
    print('Evet var')
    print(onbirinci_liste)
else:
    print('Hayır yok')
print('-----')

bos_liste = []
for i in range(1,10):
    bos_liste.append(i) #listeye eleman ekleme
print(bos_liste)
print('-----')


#ödev: isim, soyisim, tc no, doğduğu yer boş listeye değişkenle ekle

