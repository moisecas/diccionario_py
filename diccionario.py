def violeta():
    mi_diccionario = {
        "llave1":1,
        "llave2":2,
        "llave3":3, 
    }
    print(mi_diccionario["llave1"]) 
    print(mi_diccionario["llave2"]) 
    print(mi_diccionario["llave3"]) 

    poblacion_paises={ #llaves necesarias para definir el diccionario
        "argentina":44000000, #definimos el contenido de las variables del diccionario, al final ,
        "Brasil":210000000,
        "Colombia":48000000, 
    
    }
    print(poblacion_paises["Colombia"]) 
    for pais in poblacion_paises.keys(): #metodo de diccionario que devuelve las llaves
        print(pais) 

    for pais in poblacion_paises.values(): #metodo para mostrar el valor de las llaves
        print(pais) 

    for pais, poblacion in poblacion_paises.items(): #metodo de diccionario que devuelve las llaves y valores
        print(pais +  " tiene "  + str(poblacion) + " habitantes") #usar str para convertir el tipo de dato 


if __name__=="__main__":
    violeta() 