#1. Escriba un programa que almacene (Input) en una 
#Lista las materias que has cursado con sus respectivas notas.
#Luego muestre la lista por consola mediante un ciclo.


def  lista():
    Saludo = """
    Este programa te permite almacenar las materias que as cursado con sus respectivas notas.

    """
    print(Saludo)
    lista_cursos = ["Matematicas",5,"Ciencias",2.5,"Sociales", 5]
    def agregar():

        opcion = str(input("Deseas agregar una materias: Si(S) o No(N)): "))

        if opcion == "S":
            lista_cursos.append(input("Digite el nombre de la materia: "))
            lista_cursos.append(float(input("Digite la nota del curso: ")))
            print("Felicidades has agregado un curso con su nota :)")
            agregar()

        elif opcion == "N":
            print("")
            print("Los cursos son: ")
            print("")

            for z in lista_cursos:
                print(z)
        else:
            print("Algo salio mal")
            print("Vuelve a intentarlo")
            agregar()

        

    agregar()

#lista()

def person():
    Saludo = """

    Bienvenido al programa que te permite almacenar los nonbres de las personas.

    """
    print(Saludo)

    lista_personas = []

    def agregar_personas():

        opcion = str(input("Deseas agregar un nombre: Si(S) o No(N)): "))

        if opcion == "S":
            lista_personas.append(input("Digite el nombre se la persona: "))

            print("Felicidades has agregado un nuevo nombre)")
            agregar_personas()

        elif opcion == "N":
            print("")
            print("Los nombres son: ")
            print("")

            for z in lista_personas:
                print("Su nombre es: ")
                print(z)
        else:
            print("Algo salio mal")
            print("Vuelve a intentarlo")
            agregar_personas()

    agregar_personas()

#person()

   

#3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores 
#{'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y el valor en pesos a convertir. Luego muestre en consola el 
#símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.

def conver_divisas():
    Saludo = """

    Bienvenido al programa que te permite convertir tus divisas.

    """
    print(Saludo)

    # Definir el diccionario de divisas y sus símbolos
    divisas = { 
        'Euro': '€', 
        'Dollar': '$', 
        'Yen': '¥'
        }

    # Solicitar al usuario la divisa
    divisa = str(input("Ingrese una divisa (Euro, Dollar o Yen): "))
    valor_divisa = float(input("Digite la cantidad de pesos de la divisa que desea convertir: "))
     
    if divisa == "Euro":
        convercion_euro = valor_divisa*4771
        print("La divisa es: ", divisas.get(divisa,"Lo siento, no se encontro nada"),". Su valor es de: ",convercion_euro," En pesos")
    elif divisa == "Dollar":
        convercion_dollar = valor_divisa*4111
        print("La divisa es: ", divisas.get(divisa,"Lo siento, no se encontro nada"),". Su valor es de: ",convercion_dollar," En pesos")
    elif divisa == "Yen":
        convercion_yen = valor_divisa*28.19
        print("La divisa es: ", divisas.get(divisa,"Lo siento, no se encontro nada"),". Su valor es de: ",convercion_yen," En pesos")
    else:
        print("No esta en el diccionario")   

#conver_divisas()

#4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
#decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable son los valores digitados.
    
def tupla_tipe():

    tupa = (2, 4.5, "juan", [2, 5])

    for item in tupa:
        tipo = type(item).__name__
        print(f"El valor '{item}' es de tipo: {tipo}")

#tupla_tipe()
    




