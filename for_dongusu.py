sayac=0
sayi=input('sayi giriniz:')
for i in range (2,int(sayi)):
    if(int(sayi)%i==0):
        sayac+=1
        break
if(sayac!=0):
    print('sayı asal değil')
else:
    print('sayı asal')