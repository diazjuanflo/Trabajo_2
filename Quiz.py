

def  lista():
    Saludo = """
    Este programa te permite almacenar las materias que as cursado con sus respectivas notas.

    """
    lista_cursos = ["Matematicas",5,"Ciencias",2.5,"Sociales", 5]
    print(Saludo)
    opcion = str(input("Deseas agregar una materias: Si(S o No(N)): "))

    if opcion == "S":
        lista_cursos.append(input("Digite el nombre de la materia: "))
        lista_cursos.append(float(input("Digite la nota del curso: ")))
        print("Felicidades has agregado un curso con su nota :)")

    elif opcion == "N0":
        exit

    for z in lista_cursos:
        print(z)

def person():
    Saludo = """

    Bienvenido al programa que te permite almacenar los nonbres de las personas.

    """
    print(Saludo)

    lista = []
    
    
    




