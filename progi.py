import moduleFONTOS
import eredmenyFONTOS

kerdesek_lista = moduleFONTOS.KerdesBeolvasas()

for i in range(len(kerdesek_lista)):
    print(f"(a) {kerdesek_lista[i].valasz1}\n(b) {kerdesek_lista[i].valasz2}\n(c) {kerdesek_lista[i].valasz3}")
    kerdesek = input(f"{kerdesek_lista[i].kerdes} (a,b,c)")
    while not (kerdesek == "a" or kerdesek == "b" or kerdesek == "c"):
        print("Hibás Válasz (a,b,c)")
        kerdesek = input(f"{kerdesek_lista[i].kerdes} (a,b,c)")
    eredmenyFONTOS.PontokValasz(int(kerdesek_lista[i].Pontok(kerdesek)))
    print("\n")

print(f"Pontjaid: {eredmenyFONTOS.PontokValasz()}")
print(f"\n{eredmenyFONTOS.PontokValasz()}")
print(f"Légy tudatos, egy életünk van. Javasoljuk, hogy a gyorsan felszívódó szénhidrátokat (vagy épp a szupergyorsan felszívódókat)"
      f" -mint a nassok, sütemények, krumpli, rizs- cseréld lassan felszívódó szénhidrátokra – basmati rizs, hajdina, köles, kuszkusz- és fogyassz elég folyadékot."
      f" Minden nap legalább egy 4km-es távot sétálj le gyorssétával. Ha azt érzed, hogy nehézkes az alvás, akkor lefekvés előtt egy 30 perccel már ne nézz tv"
      f"-t és ne használd a telefonodat sem. Így nyugodtabb lesz az alvásod és másnap nem kelsz fáradtan, ami miatt amúgy összezabálsz mindent.")
