czy_pada = True
while czy_pada:
    print("ej bo, ")
    odpowiedz = input("czy dzisiaj pada? (t=tak, n=nie)")
    if odpowiedz == 't':
        print("SPRAWDZ ZA OKNEM POTEM ODPOWIADAJ")
    elif odpowiedz == 'n':
        czy_pada = False     # kończymy pętlę While
    else:
        print("NO WLASNIE NIE PADA!!!! SLONECZKO JEST ")
print("nie pada.. nie pada.. a jutro ma padac")
