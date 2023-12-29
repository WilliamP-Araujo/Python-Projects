contador = 1
try:
    while True:
        print(f"Contando... {contador}")
        contador += 1
except KeyboardInterrupt:
    print("\nVocê interrompeu a contagem!")
