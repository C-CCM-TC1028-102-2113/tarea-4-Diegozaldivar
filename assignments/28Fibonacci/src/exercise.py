
# Fibonacci
def main():
    index = int(input("Enter the index: "))
    #escribe tu código abajo de esta línea
    n_ant = 0
    n_sig = 1
    c = 1
    while c < index:
        suma = n_sig + n_ant
        n_ant = n_sig
        n_sig = suma
        c = c + 1
    print(suma)
        
         
if __name__ == '__main__':
    main()
