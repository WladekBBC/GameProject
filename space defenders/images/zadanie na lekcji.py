# A 

sum_podzielnych = 0 
for x in range(2, 101, 2):
    sum_podzielnych += x

print("SUMA LICZB PODZILNYCH PRZEZ 2 W ZBIORZE OD 1 DO 100 wynosi: ", sum_podzielnych)

# B
suma_kwadratow = 0
for liczba in range(1, 101):
    suma_kwadratow += liczba ** 2

print("Suma kwadratów liczb od 1 do 100 wynosi: ", suma_kwadratow)

# C
suma_poteg = 0

for wykladnik in range(1, 64):  # Począwszy od 1, aż do 63 (włącznie).
    suma_poteg += 2 ** wykladnik

print("Suma potęg liczby 2 dla wykładników od 1 do 63 wynosi:", suma_poteg)



# D
a = int(input("Podaj pierwszą liczbę całkowitą (a): "))
b = int(input("Podaj drugą liczbę całkowitą (b): "))


suma_nieparzystych = 0
if a > b:
    print("Suma liczb nieparzystych pomiędzy a i b wynosi:", suma_nieparzystych)
else:
    for liczba in range(a, b + 1):
        if liczba % 2 != 0:  # Sprawdzamy, czy liczba jest nieparzysta.
            suma_nieparzystych += liczba

    print("Suma liczb nieparzystych pomiędzy", a, "i", b, "wynosi:", suma_nieparzystych)



