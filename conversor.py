
dolar = 5.80
euro = 6.60
yuan = 1.26

print("Conversor de Moedas em Reais")
print("Moedas Disponíveis")
print("1. Dólar")
print("2. Euro")
print("3. Yuan")

value_str = input("Escolha o valor para conversão em reais (R$): ")
value = float(value_str.replace(",", "."))
option = input("Escolha uma opção para conversão: ")

if option == "1":
  converter = value / dolar
  print(f"R$ {value:.2f} = US$ {converter:.2f}")

elif option == "2":
  converter = value / euro
  print(f"R$ {value:.2f} = US$ {converter:.2f}")

elif option == "3":
  converter = value / yuan
  print(f"R$ {value:.2f} = US$ {converter:.2f}")
 
else:
  print("Opção inválida, digite uma opção correta")