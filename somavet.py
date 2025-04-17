N=int(input("Quantos numeros voce vai digitar: "))
vet=[0 for x in range (N)]
for i in range(0,N):
    vet[i]=float(input("Digite um numero: "))

print("Valores=")
for i in range(0,N):
    print(vet[i])
soma=0
for i in range(0,N):
    soma=soma+vet[i]
print("Soma= ",soma)

media=soma/N
print("Media= ",media)