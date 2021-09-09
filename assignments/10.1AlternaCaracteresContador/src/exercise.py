#Alterna carácteres Github
def main():
  #escribe tu código abajo de esta línea
  n =int(input(' Ingresa un valor: '))
  p = '-#'
  x = '-%'
  c = 1
  while n >= c :
      if c % 2 == 0:
          print(c, p)
      else:
          print(c, x)
      c = c + 1
