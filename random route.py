from random import randint
from random import seed
from time import time

seed(time())

# Pestről induló utak
value = randint(1,16)
if value == 8:
    print("M1")
elif value == 9:
    print("M3")
elif value == 12:
    print("M5")
elif value == 13:
    print("M6")
elif value == 14:
    print("M7")
elif value == 15:
    print("31")
elif value == 16:
    print("51")
else: print(value)

# 1-es út
if value == 1 or value == 8:
    value2 = randint(1,5)
    if value2 == 1:
        print("Tatabánya")
    if value2 == 2:
       print("Komárom")
       value3 = randint(1,2)
       if value3 == 1:
            print("13")
            print("Nagyigmánd")
    if value2 == 3:
        print("Győr")
        value3 = randint(1,3)
        if value3 == 1:
            print("14")
            print("Vámosszabadi")
        if value3 == 2:
            print("85")
            value4 = randint(1,5)
            if value4 == 1:
                print("Enese")
            if value4 == 2:
                print("Csorna")
                value5 = randint(1,2)
                if value5 == 1:
                    print("86")
                    value6 = randint(1,6)
                    if value6 == 1:
                        print("Szil")
                    if value6 == 2:
                        print("Répcelak")
                    if value6 == 3:
                        print("Szombathely")
                    if value6 == 4:
                        print("Körmend")
                    if value6 == 5:
                        print("Zalalövő")
                    if value6 == 6:
                        print("Rédics")
            if value4 == 3:
                print("Kapuvár")
            if value4 == 4:
                print("Fertőszentmiklós")
            if value4 == 5:
                print("Sopron")
    if value2 == 4:
        print("Mosonmagyaróvár")
        value3 = randint(1,2)
        if value3 == 1:
            print("15")
            print("Rajka")
    if value2 == 5:
        print("Hegyeshalom")

# 2-es út
if value == 2:
    value2 = randint(1,3)
    if value2 == 1:
        print("Vác")
        print("12")
        value3 = randint(1,3)
        if value3 == 1:
            print("Nagymaros")
        if value3 == 2:
            print("Szob")
        if value3 == 3:
            print("Kemence")
    if value2 == 2:
        print("Rétság")
        print("22")
        value3 = randint(1,3)
        if value3 == 1:
            print("Balassagyarmat")
        if value3 == 2:
            print("Szécsény")
        if value3 == 3:
            print("Salgótarján")
    if value2 == 3:
        print("Hont")

# 3-as út
if value == 3:
    value2 = randint(1,6)
    if value2 == 1:
        print("Hatvan")
        value3 = randint(1,3)
        if value3 == 1:
            print("32")
            value4 = randint(1,2)
            if value4 == 1:
                print("Jászberény")
            if value4 == 2:
                print("Szolnok")
        if value3 == 2:
            print("21")
            value4 = randint(1,3)
            if value4 == 1:
                print("Pásztó")
            if value4 == 2:
                print("Bátonyterenye")
                print("23")
                print("Pétervására")
            if value4 == 3:
                print("Salgótarján")
    if value2 == 2:
        print("Gyöngyös")
        value3 = randint(1,2)
        if value3 == 1:
            print("24")
            value4 = randint(1,3)
            if value4 == 1:
                print("Kékestető")
            if value4 == 2:
                print("Recsk")
            if value4 == 3:
                print("Eger")
    if value2 == 3:
        print("Kápolna")
        value3 = randint(1,2)
        if value3 == 1:
            print("25")
            value4 = randint(1,5)
            if value4 == 1:
                print("Eger")
            if value4 == 2:
                print("Szarvaskő")
            if value4 == 3:
                print("Borsodnádasd")
            if value4 == 4:
                print("Ózd")
            if value4 == 5:
                print("Bánréve")
    if value2 == 4:
        print("Füzesabony")
        value3 = randint(1,2)
        if value3 == 1:
            print("33")
            value4 = randint(1,3)
            if value4 == 1:
                print("Tiszafüred")
            if value4 == 2:
                print("Hortobágy")
            if value4 == 3:
                print("Debrecen")
    if value2 == 5:
        print("Nyékládháza")
        value3 = randint(1,2)
        if value3 == 1:
            print("35")
            value4 = randint(1,4)
            if value4 == 1:
                print("Tiszaújváros")
            if value4 == 2:
                print("Hajdúböszörmény")
            if value4 == 3:
                print("Polgár")
                value5 = randint(1,2)
                if value5 == 1:
                    print("36")
                    value6 = randint(1,2)
                    if value6 == 1:
                        print("Tiszavasvári")
                    if value6 == 2:
                        print("Nyíregyháza")
            if value4 == 4:
                print("Debrecen")
    if value2 == 6:
        print("Miskolc")
        value3 = randint(1,3)
        if value3 == 1:
            print("26")
            value4 = randint(1,2)
            if value4 == 1:
                print("Kanzincbarcika")
            if value4 == 2:
                print("Bánréve")
        if value3 == 2:
            print("37")
            value4 = randint(1,2)
            if value4 == 1:
                print("Szerencs")
            if value4 == 2:
                print("Sárospatak")
    if value2 == 7:
        print("Encs")
        value3 = randint(1,2)
        if value3 == 1:
            print("39")
            value4 = randint(1,2)
            if value4 == 1:
                print("Abaújszántó")
            if value4 == 2:
                print("Mád")
    if value2 == 8:
        print("Tornyosnémeti")

# M3
if value == 9:
    value2 = randint(1,6)
    if value2 == 1:
        print("Hatvan")
    if value2 == 2:
        print("Füzesabony")
        print("M25")
        print("Eger")
    if value2 == 3:
        print("Nyékládháza")
        print("M30")
        print("Miskolc")
    if value2 == 4:
        print("Görbeháza")
        print("M35")
        value3 = randint(1,3)
        if value3 == 1:
            print("Hajdúböszörmény")
        if value3 == 2:
            print("Debrecen")
        if value3 == 3:
            print("Berettyóújfalu")
    if value2 == 5:
        print("Nyíregyháza")
    if value2 == 6:
        print("Vásárosnamény")

# 4-es út
if value == 4:
    value2 = randint(1,9)
    if value2 == 1:
        print("Cegléd")
    if value2 == 2:
        print("Szolnok")
    if value2 == 3:
        print("Törökszentmiklós")
        value3 = randint(1,2)
        if value3 == 1:
            print("46")
            value4 = randint(1,3)
            if value4 == 1:
                print("Mezőtúr")
            if value4 == 2:
                print("Gyomaendrőd")
            if value4 == 3:
                print("Mezőberény")
    if value2 == 4:
        print("Fegyvernek")
        value3 = randint(1,2)
        if value3 == 1:
            print("34")
            value4 = randint(1,3)
            if value4 == 1:
                print("Kunhegyes")
            if value4 == 2:
                print("Kunmadaras")
            if value4 == 3:
                print("Tiszafüred")
    if value2 == 5:
        print("Püspökladány")
        value3 = randint(1,2)
        if value3 == 1:
            print("42")
            value4 = randint("1,3")
            if value4 == 1:
                print("Földes")
            if value4 == 2:
                print("Berettyóújfalu")
            if value4 == 3:
                print("Biharkeresztes")
    if value2 == 6:
        print("Debrecen")
        value3 = randint(1,3)
        if value3 == 1:
            print("47")
            value4 = randint(1,6)
            if value4 == 1:
                print("Berettyóújfalu")
            if value4 == 2:
                print("Szeghalom")
            if value4 == 3:
                print("Békéscsaba")
            if value4 == 4:
                print("Orosháza")
            if value4 == 5:
                print("Hódmezővásárhely")
            if value == 6:
                print("Szeged")
        if value3 == 2:
            print("48")
            print("Vámospércs")
    if value2 == 7:
        print("Nyíregyháza")
        value3 = randint(1,2)
        if value3 == 1:
            print("41")
            value4 = randint(1,3)
            if value4 == 1:
                print("Levelek")
            if value4 == 2:
                print("Rohod")
                value5 = randint(1,2)
                if value5 == 1:
                    print("49")
                    value6 = randint(1,2)
                    if value6 == 1:
                        print("Mátészalka")
                    if value6 == 2:
                        print("Csengersima")
            if value4 == 3:
                print("Beregsurány")
    if value2 == 8:
        print("Kisvárda")
    if value2 == 9:
        print("Záhony")

# 5-ös út
if value == 5 or value == 12:
    value2 = randint(1,5)
    if value2 == 1:
        print("Dabas")
        value3 = randint(1,2)
        if value3 == 1:
            print("405")
            print("Albertirsa")
    if value2 == 2:
        print("Kecskemét")
        value3 = randint(1,5)
        if value3 == 1:
            print("441")
            print("Cegléd")
        if value3 == 2:
            print("44")
            value4 = randint(1,4)
            if value4 == 1:
                print("Kunszentmárton")
                value5 = randint(1,2)
                if value5 == 1:
                    print("Szentes")
                if value5 == 2:
                    print("Hódmezővásárhely")
            if value4 == 2:
                print("Szarvas")
            if value4 == 3:
                print("Békéscsaba")
            if value4 == 4:
                print("Gyula")
        if value3 == 3:
            print("54")
            value4 = randint(1,3)
            if value4 == 1:
                print("Soltvadkert")
            if value4 == 2:
                print("Kecel")
            if value4 == 3:
                print("Sükösd")
        if value3 == 4:
            print("52")
            value4 = randint(1,3)
            if value4 == 1:
                print("Fülöpszállás")
            if value4 == 2:
                print("Solt")
            if value4 == 3:
                print("Dunaföldvár")
    if value2 == 3:
        print("Kiskunfélegyháza")
        value3 = randint(1,2)
        if value3 == 1:
            print("451")
            value4 = randint(1,2)
            if value4 == 1:
                print("Csongrád")
            if value4 == 2:
                print("Szentes")
    if value2 == 4:
        print("Szeged")
        value3 = randint(1,3)
        if value3 == 1:
            print("43")
            value4 = randint(1,2)
            if value4 == 1:
                print("Makó")
            if value4 == 2:
                print("Nagylak")
        if value3 == 2:
            print("55")
            value4 = randint(1,5)
            if value4 == 1:
                print("Mórahalom")
            if value4 == 2:
                print("Mélykút")
            if value4 == 3:
                print("Csávoly")
            if value4 == 4:
                print("Baja")
            if value4 == 5:
                print("Bátaszék")
    if value2 == 5:
        print("Röszke")

# 6-os út
if value == 6:
    value2 = randint(1,10)
    if value2 == 1:
        print("Százhalombatta")
    if value2 == 2:
        print("Dunaújváros")
        value3 = randint(1,2)
        if value3 == 1:
            print("62")
            value4 = randint(1,2)
            if value4 == 1:
                print("Szabadegyháza")
            if value4 == 2:
                print("Székesfehérvár")
    if value2 == 3:
        print("Dunaföldvár")
        value3 = randint(1,2)
        if value3 == 1:
            print("61")
            value4 = randint(1,7)
            if value4 == 1:
                print("Cece")
            if value4 == 2:
                print("Simontornya")
            if value4 == 3:
                print("Tamási")
            if value4 == 4:
                print("Dombóvár")
            if value4 == 5:
                print("Kaposvár")
            if value4 == 6:
                print("Böhönye")
            if value4 == 7:
                print("Nagykanizsa")
    if value2 == 4:
        print("Paks")
    if value2 == 5:
        print("Szekszárd")
        value3 = randint(1,3)
        if value3 == 1:
            print("56")
            value4 = randint(1,3)
            if value4 == 1:
                print("Bátszék")
            if value4 == 2:
                print("Mohács")
            if value4 == 3:
                print("Udvar")
        if value3 == 2:
            print("65")
            value4 = randint(1,3)
            if value4 == 1:
                print("Hőgyész")
            if value4 == 2:
                print("Tamási")
            if value4 == 3:
                print("Siófok")
    if value2 == 6:
        print("Bonyhád")
    if value2 == 7:
        print("Pécsvárad")
    if value2 == 8:
        print("Pécs")
        value3 = randint(1,2)
        if value3 == 1:
            print("66")
            value4 = randint(1,2)
            if value4 == 1:
                print("Sásd")
            if value4 == 2:
                print("Kaposvár")
    if value2 == 9:
        print("Szigetvár")
        value3 = randint(1,2)
        if value3 == 1:
            print("67")
            value4 = randint(1,4)
            if value4 == 1:
                print("Szentlászló")
            if value4 == 2:
                print("Kaposvár")
            if value4 == 3:
                print("Mernye")
            if value4 == 4:
                print("Balatonszemes")
    if value2 == 10:
        print("Barcs")

# M6/M60
if value == 13:
    value2 = randint(1,4)
    if value2 == 1:
        print("Dunaújváros")
    if value2 == 2:
        print("Paks")
    if value2 == 3:
        print("Szekszárd")
    if value2 == 4:
        print("Mohács")
        value3 = randint(1,2)
        if value3 == 1:
            print("M60")
            print("Pécs")

# 7-es út
if value == 7 or value == 14:
    value2 = randint(1,11)
    if value2 == 1:
        print("Martonvásár")
    if value2 == 2:
        print("Velence")
    if value2 == 3:
        print("Székesfehérvár")
        value3 = randint(1,5)
        if value3 == 1:
            print("62")
            value4 = randint(1,2)
            if value4 == 1:
                print("Szabadegyháza")
            if value4 == 2:
                print("Dunaújváros")
        if value3 == 2:
            print("63")
            value4 = randint(1,6)
            if value4 == 1:
                print("Sárkeresztúr")
            if value4 == 2:
                print("Sárbogárd")
            if value4 == 3:
                print("Cece")
            if value4 == 4:
                print("Nagydorog")
            if value4 == 5:
                print("Szedres")
            if value4 == 6:
                print("Szekszárd")
        if value3 == 3:
            print("8")
            value4 = randint(1,6)
            if value4 == 1:
                print("Veszprém")
                value5 = randint(1,4)
                if value5 == 1:
                    print("82")
                if value5 == 2:
                    print("73")
                if value5 == 3:
                    print("77")
            if value4 == 2:
                print("Városlőd")
            if value4 == 3:
                print("Jánosháza")
            if value4 == 4:
                print("Kám")
            if value4 == 5:
                print("Körmend")
            if value4 == 6:
                print("Rábafüzes")
        if value3 == 4:
            print("81")
    if value2 == 4:
        print("Lepsény")
        value3 = randint(1,3)
        if value3 == 1:
            print("64")
            value4 = randint(1,2)
            if value4 == 1:
                print("Dég")
            if value4 == 2:
                print("Simontornya")
        if value3 == 2:
            print("71")
            value4 = randint(1,5)
            if value4 == 1:
                print("Balatonalmádi")
            if value4 == 2:
                print("Balatonfüred")
            if value4 == 3:
                print("Balatonszepezd")
            if value4 == 4:
                print("Balatonederics")
                value5 = randint(1,2)
                if value5 == 1:
                    print("84")
                    value6 = randint(1,6)
                    if value6 == 1:
                        print("Sümeg")
                    if value6 == 2:
                        print("Duka")
                    if value6 == 3:
                        print("Sárvár")
                        value7 = randint(1,2)
                        if value7 == 1:
                            print("88")
                            print("Szombathely")
                    if value6 == 4:
                        print("Újkér")
                    if value6 == 5:
                        print("Nagycenk")
                    if value6 == 6:
                        print("Sopron")
            if value4 == 5:
                print("Keszthely")
    if value2 == 5:
        print("Siófok")
        value3 = randint(1,2)
        if value3 == 1:
            print("65")
            value4 = randint(1,3)
            if value4 == 1:
                print("Tamási")
            if value4 == 2:
                print("Hőgyész")
            if value4 == 3:
                print("Szekszárd")
    if value2 == 6:
        print("Balatonszemes")
        # 67; Mernye, Kaposvár, Szentlászló, Szigetvár
    if value2 == 7:
        print("Fonyód")
    if value2 == 8:
        print("Balatonkeresztúr")
        # 68; Marcali, Böhönye, Nagyatád, Barcs
        # 76; Sármellék, Zalacsány, Zalaegerszeg, Nádasd
    if value2 == 9:
        print("Sávoly")
    if value2 == 10:
        print("Nagykanizsa")
        # 74; Bak, Zalaegerszeg, Vasvár
    if value2 == 11:
        print("Letenye")