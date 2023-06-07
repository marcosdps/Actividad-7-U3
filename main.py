from clasePersonal import Personal
from claseDocente import Docente
from claseApoyo import PersonalApoyo
from listaPersonal import ListaPersonal
from objectEncoder import ObjectEncoder


def acceso(opcion):
    if opcion == 10:
        usuario= input("Usuario: ")
        clave= input("Clave: ")
        if usuario == "uDirector" and clave == "ufC77#!1":
            lista.director()
    else:
        print("Algo")

if __name__ == "__main__":
    lista = ListaPersonal()
    jsonf = ObjectEncoder()
    diccionario = jsonf.leerArchivoJSON("personal.json")
    #print(diccionario)
    agente = jsonf.decodificador(diccionario,lista)
    interfaz = """\n---------MENU DE OPCIONES---------
    -1- Insertar agente en la coleccion
    -2- Agregar agente a la coleccion
    -3- Mostrar tipo de agente dada una posicion
    -4- Generar listado ordenado por nombre de Docentes Investigadores
    -5- Contar cantidad de agentes que son docente investigador, y la cantidad de investigadores que trabajen en un área.
    -6- Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.
    -7- Mostrar datos de agentes de una categoria y el monto total de esa categoria
    -8- Guardar datos en json
    -9- Mostrar datos de la coleccion
    -10- MENU DE OPCIONES - DIRECTOR
    -11- Consultar sueldo de agente - TESORERO
    -0- SALIR"""
    print(interfaz)
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 0:
        match opcion:
            case 1:
                posicion = int(input("Ingrese la posicion: "))
                if posicion <= lista.getTope():
                    tipo = input("Ingrese tipo: Docente, Investigador, Docente Investigador, Personal de Apoyo\n")
                    agente = lista.ingresarDatos(tipo)
                    lista.insertarElemento(posicion, agente)
            case 2:
                tipo = input("Ingrese tipo: Docente, Investigador, Docente Investigador, Personal de Apoyo\n")
                agente = lista.ingresarDatos(tipo)
                lista.agregarElemento(agente)
            case 3:
                posicion = int(input("Ingrese la posicion: "))
                if posicion <= lista.getTope():
                    lista.mostrarElemento(posicion)
            case 4:
                carrera = input("Nombre de carrera: ")
                lista.nuevaLista(carrera)
            case 5:
                areaDeInvestigacion = input("Ingrese area de investigacion: ")
                lista.contarDocentesYtrabajadores(areaDeInvestigacion)
            case 6:
                lista.generarListaOrdenadaYmostrar()
            case 7:
                categoria = input("Ingrese una categoria(I,II,III,IV,V): ")
                lista.calculoImporteYmostrarDatos(categoria)
            case 8:
                d=lista.toJSON()
                jsonf.guardarDatos(d)
            case 9:
                lista.mostrarDatos()
            case 10:
                acceso(opcion)
            case 11:
                acceso(opcion)
                print("Usted es tesorero")
        print(interfaz)
        opcion = int(input("Ingrese una opcion: "))

