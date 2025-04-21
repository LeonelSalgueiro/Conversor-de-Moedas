
dolar = 5.80
euro = 6.60
yuan = 1.26

while True:
 print("Conversor de Moedas em Reais")
 print("Moedas Disponíveis")
 print("1. Dólar")
 print("2. Euro")
 print("3. Yuan")
 print("4. Sair")

 valor = float(input("Escolha o valor para conversão em reais (R$): "))
 escolha = input("Escolha uma opção para conversão: ")
 

 if escolha == "1":
  conversor = valor / dolar
  print(f"R$ {valor:.2f} = US$ {conversor:.2f}")

 elif escolha == "2":
  conversor = valor / euro
  print(f"R$ {valor:.2f} = US$ {conversor:.2f}")

 elif escolha == "3":
  conversor = valor / yuan
  print(f"R$ {valor:.2f} = US$ {conversor:.2f}")

 elif escolha == "4":
  break
 
 else:
  print("Opção inválida, digite uma opção correta")