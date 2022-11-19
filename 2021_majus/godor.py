import math
import matplotlib.pyplot as plt

def main():
    lines = open("./melyseg.txt", 'r').readlines()
    melysegek = []

    for line in lines:
        melysegek.append(
            int(
                line.rstrip('\n')
            )
        )

    print("1. feladat")
    print(f"A fájl adatainak száma: {melysegek.__len__()}")

    print("\n2. feladat")
    in_tav = int(input("Adjon meg egy távolságértéket! "))
    print(f"Ezen a helyen a felszín {melysegek[in_tav-1]} méter mélyen van.")

    print("\n3. feladat")
    erintetlen = list(filter(lambda x: x == 0, melysegek)).__len__()
    print(f"Az érintetlen terület aránya {round((erintetlen / melysegek.__len__()) * 100, 2)}%.")

    # 4. feladat
    out_list = []
    godrok_file = open("godrok.txt", "w")
    godrok_szama = 0
    for adat in melysegek:
        if adat == 0 and out_list.__len__() > 0:
            godrok_file.write(str(' '.join(map(lambda x: str(x), out_list)) + '\n'))
            out_list = []
            godrok_szama += 1
        elif adat != 0:
            out_list.append(adat)

    print('\n5. feladat')
    print(f'A gödrök száma: {godrok_szama}')

    print('\n6. feladat')
    print('a)')
    if melysegek[in_tav-1] == 0:
        print("Az adott helyen nincs gödör.")
    else:
        godor_kezdo = in_tav
        for i in range(in_tav-1, -1, -1):
            if melysegek[i] == 0:
                godor_kezdo = i+2
                break

        godor_vege = in_tav
        for i in range(in_tav, melysegek.__len__()):
            if melysegek[i] == 0:
                godor_vege = i
                break

        print(f"A gödör kezdete: {godor_kezdo} méter, a gödör vége: {godor_vege} méter.")
        
        ### C
        max_melyseg_index = 0
        max_melyseg = 0
        for i in range(godor_kezdo-1, godor_vege):
            if melysegek[i] > max_melyseg:
                max_melyseg = melysegek[i]
                max_melyseg_index = i
        ###

        ### Ennél volt egy jobb/bonyolultabb megoldásom, de az informatika tanárom szerint ezt így kell megoldani....
        print('b)')
        melyul = True
        elozo = melysegek[godor_kezdo-1]
        for i in range(godor_kezdo-1, max_melyseg_index+1):
            if melysegek[i] >= elozo:
                melyul = False
                break
            elozo = melysegek[i]

        if melyul:
            elozo = melysegek[max_melyseg_index]
            for i in range(max_melyseg_index, godor_vege):
                if melysegek[i] <= elozo:
                    melyul = False
                    break
                elozo = melysegek[i]

        print("Folyamatosan mélyül." if melyul else "Nem mélyül folyamatosan.")


        print('c)')
        print(f"A legnagyobb mélysége {max_melyseg} méter.")

        print('d)')
        melyseg_sum = 0
        for i in range(godor_kezdo-1, godor_vege):
            melyseg_sum += melysegek[i]
        print(f"A térfogata {melyseg_sum * 10} m^3.")

        print("e)")
        melyseg_sum = 0
        for i in range(godor_kezdo-1, godor_vege):
            melyseg_sum += (melysegek[i] - 1)
        print(f"A vízmennyiség {melyseg_sum * 10} m^3.")

        plt.bar(
            range(0, (godor_vege - godor_kezdo + 1)),
            melysegek[(godor_kezdo - 1):godor_vege]
        )
        plt.show()

main()