
angka=int(input("ketikan angka = "))
def kategoribil(angka):
    listkosong =list()
    if angka == angka and angka== complex(angka):
        listkosong.append('bilangan bulat')
        
    if angka!= complex(angka):
        listkosong.append('bilangan cacah')
        
    if angka== complex(angka):
        listkosong.append('bilangan negatif')
        
    if angka== 0:
        listkosong.append('bilangan nol')
       
    if angka!=complex(angka) and angka!= 0:
        bilanganasli=angka!=complex(angka) and angka!= 0
        listkosong.append('bilangan asli')
        
    if (angka %2 == 0 )and (angka>0):
        listkosong.append('bilangan genap')
         
    if angka %2 != 0 and angka>0:
        listkosong.append('bilangan ganjil')
        
    if angka > 1:
        for i in range(2,angka):
            if (angka % i) == 0:
                listkosong.append('Komposit')
                break
        else:
            listkosong.append('Prima')
    return listkosong
        


print(kategoribil(angka))
