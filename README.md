# numeros de la loteria 

loteria= ("cuales son los numeros ganadores ")

numeros = []

# cuales son los seeis numeros ganadores 
for i in range (6):
    num = int(input(f"ingrese el ganador {i+1}:"))
    numeros.append(num)
    
    # lista 
numeros.sort()

#ordenados
print("Números  de menor a mayor:")
print(numeros)
    
    
