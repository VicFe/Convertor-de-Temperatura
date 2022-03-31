# Convertor-de-Temperatura

Convertor = input("Escolha a temperatura que será convertida: Fahrenheit (F) / Celsius (C)")

if Convertor == "F":
    Fahrenheit = int(input("Digite o valor em Fahrenheit que sera convertido em Celsius: "))
    Celsius = 5 * ((Fahrenheit-32)/9)
    print ("C = 5 * (({}-32)/9)".format(Fahrenheit))
    print ("Resultado: ", Celsius)
if Convertor == "C":
    Celsius = int(input("Digite o valor em Celsius que sera convertido em Fahrenheit: "))
    Fahrenheit = (Celsius*9/5) + 32
    print ("F = ({}*9/5) + 32".format(Celsius))
    print ("Resultado: ", Fahrenheit)

Febre = input("Você gostaria de saber se está com febre ou não?. Se sim digite (S) se não digite (N): ")

if Febre == "S":
    if Convertor == "F":
        if Celsius >= 39:
            print ("Você está com Febre \n")
        if Celsius <= 36:
            print ("Você não está com Febre \n")
    if Convertor == "C":
        if Fahrenheit >= 99.5:
            print ("Você está com Febre \n")
        if Fahrenheit <= 99:
            print ("Você não está com Febre \n")
if Febre == "N":
    print(":( \n")
