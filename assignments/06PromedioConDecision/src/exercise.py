def main():
  #escribe tu código abajo de esta línea
  suma_total = 0
  contador = 0
  promedio = 0
  n = 0
  while n >= 0:
      n = float(input(' Ingresa un valor: '))
      if n < 0:
          break
      else:
           contador = contador + 1
           suma_total = suma_total + n
  promedio = suma_total / contador
  print(promedio)



if __name__ == '__main__':
    main()
