def get_texto():
    text = input("Por favor ingresa el texto con el que se requiere trabajar:")
    return text


def search_letter_on_text():
    parrafo = get_texto()
    list_caracteres = []
    dic_contador={}
    cont = 0
    numerocarcateres = input("\nIngresa el numero de Caracteres que quieres buscar\n")
    numcarcateres = int(numerocarcateres)
    for i in range(numcarcateres):
        letra = input(f"\nIngrese la letra numero {i}\n")
        list_caracteres.append(letra)
    for item in list_caracteres:
        dic_contador[item] = parrafo.count(item)

    print(dic_contador)


def count_word():
    text = get_texto()
    word_count = len(text.split())
    print(f"--> tiene {word_count} palabras")


def first_and_last_word():
    text = get_texto()
    first_word = text.split()[0]
    last_word = text.split()[-1]
    print(f"--> la priemra palabra es {first_word} y la ultima palabra es {last_word}")


def reversed_text():
    text = get_texto()
    reversed = text[::-1]
    print(reversed)


def find():
    text = get_texto()
    if text.find("Python") > 0:
        print("--> la palabra si se encuentra en el parrafo")
    else:
        print("--> la palabra no se encuentra en el parrafp")

def show_menu():
    try:
        opcion = input("\nSelecciona la opcion que desees realizar\n"
                       "1- Cuantas veces aparce un caracter en el texto\n"
                       "2- Contar palabras tiene el texto\n"
                       "3- Primera y ultima letra del texto\n"
                       "4- Texto invertido\n"
                       "5- Buscar la palabra 'Python' en el texto\n"
                       "6- Salir\n")
        match opcion:
            case "1":
                search_letter_on_text()
            case "2":
                count_word()
            case "3":
                first_and_last_word()
            case "4":
                reversed_text()
            case "5":
                find()
            case "6":
                exit()
    except EnvironmentError:
        print("Error")


show_menu()
