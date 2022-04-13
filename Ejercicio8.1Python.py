#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. 
# Para ello, tendréis que acceder dos veces al archivo creado.

f=open('miarchivo.txt','w')


def escribe(fichero,datos):
    f=open(fichero,'w')
    
    for linea in datos:
        if not linea.endswith('\n'):
            linea=linea + '\n'
        
        f.write(linea)



    f.close()

lista=[
    '1',
    '2',
    '3'
]

escribe('mifichero.txt',lista)