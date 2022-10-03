

import random



print("****************************************" "\n")
print("<<<<<<<<<<<<-İSTİNYE KOMBAT->>>>>>>>>>>> " "\n")
print("****************************************" "\n")

while True:    
    ilk_kahraman_adi = input ("--------- İlk Kahraman --------- \n Lütfen Kahramanınızın adını yazın: ")
    if len(ilk_kahraman_adi) > 1:
        print ("\n Birinci kahramanın adı:", ilk_kahraman_adi.capitalize())
        break
    else:
        print( "Kahramanın adının uzunluğu 1 karakterden uzun olmalıdır.")

while True:    
    ikinci_kahraman_adi = input("--------- İkinci Kahraman --------- \n Lütfen Kahramanınızın adını yazın: ")
    if len(ikinci_kahraman_adi) <= 1:
        print ("Kahramanın adının uzunluğu 1 karakterden uzun olmalıdır."  )      
    elif ikinci_kahraman_adi == ilk_kahraman_adi:
        print (ilk_kahraman_adi, "alındı,lütfen başka bir isim seçin!")

    else:
        print("\n İkinci kahramanın adı:", ikinci_kahraman_adi.capitalize())
        break

oyuncu_listesi = [ilk_kahraman_adi, ikinci_kahraman_adi]
yazı_tura = random.choice(oyuncu_listesi)
oyuncu_listesi.remove(yazı_tura)
print ("\n Yazı tura sonucu: %s önce başlar!" %yazı_tura.capitalize()) 


def attack1(current_hp):
    hp2 = current_hp
    zarar_sansi=random.randint(0,100)
    print( "\n --------------- %s Saldırı !! ---------------"  %yazı_tura.capitalize())
    while True:
        saldiri_derecesi = input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin: ")
        saldiri_derecesi = float(saldiri_derecesi)

        if saldiri_derecesi > 50:
            print ("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır..")

        elif saldiri_derecesi < 1:
            print ("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır..")
        else:
            break


    while True:
        if zarar_sansi > saldiri_derecesi:
            print (yazı_tura, " %s hasar verdi!!"%saldiri_derecesi)
            hp2=hp2-saldiri_derecesi
            return hp2
        else:
            print (" Ooopsy! %s saldırıyı kaçırdı!"%yazı_tura.capitalize())
            return hp2

def attack2(current_hp):
    hp1=current_hp
    zarar_sansi=random.randint(0,100)
    print ("\n --------------- %s Saldırı !! ---------------"%oyuncu_listesi)
    while True:
        saldiri_derecesi=input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin: ")
        saldiri_derecesi=int(saldiri_derecesi)
        
        if saldiri_derecesi > 50:
            print ("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır..")

        elif saldiri_derecesi < 1:
            print ("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır..")
        else:
            break


    while True:
        if zarar_sansi > saldiri_derecesi:
            print (oyuncu_listesi, " %s hasar verdi!!"%saldiri_derecesi)
            hp1=hp1-saldiri_derecesi
            return hp1
        else:
            print ("Ooopsy! %s saldırıyı kaçırdı!"%oyuncu_listesi)
            return hp1

def main():
    hp1, hp2 = (100,100)
    while hp2<=1:
        print (oyuncu_listesi, "Kazanan")
        break

    while hp1 > 1 and hp2 > 1:
            hp1 = attack1(hp1)
            print (yazı_tura,"                                                                ", oyuncu_listesi)

            print ("HP [%s]:"%hp2, int(hp2/2) * "|" ,"        ", "HP [%s]:"%hp1, int(hp1/2) * "|" )
            hp2 = attack2(hp2)
            print (yazı_tura,"                                                                 ", oyuncu_listesi)

            print ("HP [%s]:"%hp2, int(hp2/2) * "|" ,"        ", "HP [%s]:"%hp1, int(hp1/2) * "|")

    while hp1<=1:
         print (yazı_tura, " Kazanan")
         break

main()