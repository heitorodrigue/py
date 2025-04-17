print("Digite dois numeros: ")
x=int(input())
z=int(input())
while x!=z:
    if x<z:
        print("CRESCENTE")
    else:
        print("DECRESCENTE")
    print("Digite outros dois numeros: ")
    x=int(input())
    z=int(input())
