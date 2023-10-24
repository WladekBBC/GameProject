suma_parzystych = 0

for liczba in range(2, 101, 2):
    if liczba % 2 == 0:  # Sprawdzamy, czy liczba jest parzysta.
        suma_parzystych += liczba


def power(a, n):
    wynik = 1 
    for i in range(n):
        wynik *= a

    return wynik

print(power(2, 10))