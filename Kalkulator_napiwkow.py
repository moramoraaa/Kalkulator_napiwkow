# Kalkulator napiwków

''' Napisz program Kalkulator napiwku, w którym użytkownik wprowadza sumę
ogólną z rachunku wystawionego przez restaurację. Program powinien potem
wyświetlić dwie kwoty napiwku — w wysokości 15 i 20 procent.'''

def fajnakelnerka(x):
    return x * 0.2

def brzydkakelnerka(y):
    return y * 0.15

print("Cześć! Nie wiesz ile zostawić napiwku w restauracji. Spróbuj tego programu!")

cena = float(input("Ile zapłaciłeś za swój obiad w restuarcji? Podaj kwotę bez wpisywania zł! "))

if cena == 0:
    print("Za darmo to raczej nie zjadłeś... Spróbuj jeszcze raz.")

else: 
    try:
        fajnakelnerka(cena)
        brzydkakelnerka(cena)
    except:
        print("Coś innego poszło nie tak... Spróbuj jeszcze raz.")

    print("Jeżeli kelnerka jest ładna to daj jej", round(fajnakelnerka(cena), 2), "zł")
    print("Jeżeli kelnerka jest brzydka to daj jej", round(brzydkakelnerka(cena), 2), "zł")

    print("Dziękuje za skorzystanie z programu. Z fartem!")