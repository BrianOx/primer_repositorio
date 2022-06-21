import sys
#realizar uns cript que imprima una palabra una cantidad de vecespasada por parametros
#imprimir hola 5      

if len(sys.argv) != 3:
    print("error,, necesito 2 argumentos")
else:
    for i in range(int(sys.argv[2])):
        print(sys.argv[1])



# argv: [nombrescript, parametro1, parametro2]
