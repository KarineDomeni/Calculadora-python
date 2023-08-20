def calculadora(num1, num2, operacao):
  num1 = int (input("Insira o primeiro número:"))
  num2 = int (input("Insira o segundo número:"))
  operacao = int (input("Insira a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))
    
  if operacao == 1:
    return num1 + num2
        
  elif operacao == 2: 
    return num1 - num2
 
  elif operacao == 3: 
    return num1 * num2

  elif operacao == 4:
      if num2 != 0:
          return num1 / num2
      else:
          return "Erro: não há divisão por zero"
  else:
      return 0 
 
resultado = calculadora (num1, num2, operacao)
print(resultado)
