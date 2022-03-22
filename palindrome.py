texto = input ("Digite o texto:")
texto=texto.lower()
if (texto==texto[::-1]):
    print ("É um palindromo")
else:
    print ("Não é um palindromo")
    
