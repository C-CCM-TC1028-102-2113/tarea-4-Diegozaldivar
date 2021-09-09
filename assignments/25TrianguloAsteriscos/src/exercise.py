
# Triángulo de asterísticos

def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    contador_r = 1
    contador_e = 1
    while contador_r <= height:
        while contador_e <= contador_r:
            print(" " * (height - contador_r) + "*" * contador_e)
            contador_e = contador_e + 1
        contador_r = contador_r + 1

