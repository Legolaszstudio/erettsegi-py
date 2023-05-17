from typing import List


class Ajto:
    def __init__(self, ora, perc, azonosito, irany):
        self.ora = int(ora)
        self.perc = int(perc)
        self.azonosito = int(azonosito)
        self.irany: str = irany


adatok: List[Ajto] = []

# Read file
f = open("ajto.txt", "r")
for line in f:
    sor = line.strip().split(" ")
    adatok.append(
        Ajto(*sor)
    )
f.close()

# -----------------------------
print("2. feladat")
first_in = False
first_out = False
for adat in adatok:
    if adat.irany == "be" and not first_in:
        print(f"Az első belépő: {adat.azonosito}")
        first_in = True
    elif adat.irany == "ki" and not first_out:
        print(f"Az első kilépő: {adat.azonosito}")
        first_out = True
    if first_in and first_out:
        break

# -----------------------------
# 3. feladat
f = open("athaladas.txt", "w", encoding="utf-8")
szamlalo = {}
for adat in adatok:
    if adat.azonosito not in szamlalo:
        szamlalo[adat.azonosito] = 0
    szamlalo[adat.azonosito] += 1

szamlalo = dict(sorted(szamlalo.items(), key=lambda x: x[0]))
for azonosito, db in szamlalo.items():
    f.write(f"{azonosito} {db}\n")
f.close()

# -----------------------------
print("\n4. feladat")
kibe = {}
for adat in adatok:
    kibe[adat.azonosito] = (adat.irany == "be")

bent_volt = []
for key in kibe:
    if kibe[key]:
        bent_volt.append(key)

bent_volt.sort()
bent_volt = ' '.join(list(map(lambda x: str(x), bent_volt)))

print(f"A végén a társalgóban voltak: {bent_volt}")

# -----------------------------
print("\n5. feladat")
counter = {}
counter_before = 0
for adat in adatok:
    if adat.irany == "be":
        counter_before += 1
        counter[f"{adat.ora}:{adat.perc}"] = counter_before
    else:
        counter_before -= 1
        counter[f"{adat.ora}:{adat.perc}"] = counter_before

max_seen = 0
max_seen_date = ""
for key in counter:
    if counter[key] > max_seen:
        max_seen = counter[key]
        max_seen_date = key

max_seen_date = max_seen_date.split(":")
max_seen_date = f"{max_seen_date[0]}:{max_seen_date[1].rjust(2, '0')}"

print(f"Például {max_seen_date}-kor voltak a legtöbben a társalgóban.")

# -----------------------------
print("\n6. feladat")
szemelybe = input("Adja meg a személy azonosítóját! ")

# -----------------------------
print("\n7. feladat")
szemelyFiltered = list(
    filter(lambda x: x.azonosito == int(szemelybe), adatok)
)
bent_let = 0
bent_let_kezdet = 0
for adat in szemelyFiltered:
    if adat.irany == "be":
        print(f"{adat.ora}:{adat.perc}-", end="")
        if adat == szemelyFiltered[-1]:
            print()
        bent_let_kezdet = adat.ora * 60 + adat.perc
    else:
        print(f"{adat.ora}:{str(adat.perc).rjust(2, '0')}")
        bent_let += (adat.ora * 60 + adat.perc) - bent_let_kezdet

if szemelyFiltered[-1].irany == "be":
    bent_let += (15 * 60) - bent_let_kezdet

# -----------------------------
print("\n8. feladat")
print(f"A(z) {szemelybe}. személy összesen {bent_let} percet volt bent, a megfigyelés végén {'a társalgóban volt' if szemelyFiltered[-1].irany == 'be' else 'nem volt a társalgóban'}.")
