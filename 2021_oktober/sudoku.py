import math


tabla = []
lepesek = []


def main():
    print("1. feladat")
    filename = input("Adja meg a bemeneti fájl nevét! ")
    read_file(filename)
    user_row = int(input("Adja meg egy sor számát! "))
    user_col = int(input("Adja meg egy oszlop számát! "))

    print("\n3. feladat")
    print(f"Az adott helyen szereplő szám: ",
          "Az adott helyet még nem töltötték ki." if
          tabla[user_row - 1][user_col - 1] == 0
          else tabla[user_row - 1][user_col - 1]
          )
    print(f"A hely a(z) {get_half_table(user_row, user_col)} résztáblázathoz tartozik.")

    print("\n4. feladat")
    nulla_count = 0
    for i in range(9):
        for j in range(9):
            if tabla[i][j] == 0:
                nulla_count += 1
    print(f"Az üres helyek aránya: {round((nulla_count/(9*9))*100, 1)}%")

    print("\n5. feladat")
    for lepes in lepesek:
        num = lepes[0]
        row = lepes[1]
        col = lepes[2]
        print(f"A kiválasztott sor: {row} oszlop: {col} a szám: {num}")

        if tabla[row-1][col-1] != 0:
            print("A helyet már kitöltötték.\n")
            continue
        
        # Oszlop
        solution_found = False
        for i in range(9):
            if tabla[i][col-1] == num:
                print("Az adott oszlopban már szerepel a szám.\n")
                solution_found = True
                break
        
        if solution_found:
            continue
            
        # Sor
        for j in range(9):
            if tabla[row-1][j] == num:
                print("Az adott sorban már szerepel a szám.\n")
                solution_found = True
                break

        if solution_found:
            continue

        # Résztábla
        resztabla = get_half_table(row, col)
        if resztabla == 1 or resztabla == 2 or resztabla == 3:
            i0 = 0
            ie = 3
        elif resztabla == 4 or resztabla == 5 or resztabla == 6:
            i0 = 3
            ie = 6
        elif resztabla == 7 or resztabla == 8 or resztabla == 9:
            i0 = 6
            ie = 9  
            
        if resztabla == 1 or resztabla == 4 or resztabla == 7:
            j0 = 0
            je = 3
        elif resztabla == 2 or resztabla == 5 or resztabla == 8:
            j0 = 3
            je = 6
        elif resztabla == 3 or resztabla == 6 or resztabla == 9:
            j0 = 6
            je = 9  
        
        for i in range(i0, ie):
            for j in range(j0, je):
                if tabla[i][j] == num:
                    print("A résztáblázatban már szerepel a szám.\n")
                    solution_found = True
                    break
            if solution_found:
                break

        if solution_found:
                continue
        else:
            print("A lépés megtehető.\n")

        


def get_half_table(i, j):
    # 1 oszlop
    if i <= 3 and j <= 3:
        return 1
    elif i <= 6 and j <= 3:
        return 4
    elif i <= 9 and j <= 3:
        return 7 
    
    # 2 oszlop
    if i <= 3 and j <= 6:
        return 2
    elif i <= 6 and j <= 6:
        return 5
    elif i <= 9 and j <= 6:
        return 8 

    # 3 oszlop
    if i <= 3 and j <= 9:
        return 3
    elif i <= 6 and j <= 9:
        return 5
    elif i <= 9 and j <= 9:
        return 9

    raise ValueError('Rész tábla hiba')

def to_int(n):
    return int(n)


def read_file(filename):
    f = open(filename, 'r')
    i = 1
    for line in f.readlines():
        splits = list(
            map(
                to_int,
                line.rstrip('\n').split(' ')
            )
        )
        if i <= 9:
            tabla.append(splits)
        else:
            lepesek.append(splits)
        i += 1


main()
