num = input("Digite um número inteiro: ")

try:
    if int(num) % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é impar")
except:
    print("Você digitou um número não inteiro! Tente novamente.")
    
