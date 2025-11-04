def validacion_usuario(lista): #recibe a lista
    usuario_correcto=False #variable para medir se os credenciales son correctos
    usuario = str(input("Introduce usuario: ")) #garda o usuario pedido
    contraseña = str(input("Introduce contraseña: ")) #garda o contrasinal pedido

    for i in lista: #recorre a lista dos usuarios
        if i[0] == usuario and i[1] == contraseña: #se a primeira posición (a do nome) coincide co usuario pedido e a segunda posición coincide co contrasinal pedido cambia a variable
            usuario_correcto = True
            break #non interesa seguir iterando sobre o bucle se xa se ha encontrado

    return usuario_correcto




usuarios=[["usuario1", "contrasinal1"],["usuario2", "contrasinal2"], ["usuario3", "contrasinal3"]]
print(validacion_usuario(usuarios)) #chama á función pasandolle a lista usuarios e imprime o resultado do booleano

def longitud_contrasenha(contrasinal):
    if len(contrasinal)>=8: #devuelve a lonxitde do contrasinal
        return True #devolve true
    else:
        return False #devolve false

print(longitud_contrasenha("contrasinal")) #chama a función e imprime o booleano


def validacion_maiuscula(contrasinal): #recibe o contrasinal
    maius="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" #string con todaas as maiúscula
    maiuscula=False #variable que se cambiará si hay maiúsculas
    #bucle que recorre toda a contrasinal e a cada caracter xenera outro bucle que recorre as maiusculas
    for i in contrasinal:
        for j in maius:
            if i==j: #comproba se a letra figura no string das maiusculas
                maiuscula=True #maiuscula encontrada
                break #sae do bucle das maiusculas
        if maiuscula == True: #se anteriormente encontra maiuscula
            break #sale do bucle para deixar de iterar

    return maiuscula #devolve true ou false

print(validacion_maiuscula("Contrasinal")) #chama á funcion e imprime True ou False

def validacion_numeros(contrasinal): #funciona igual que o exercicio anterior pero en vez de unha cadea con todas as letras en maiusculas unha cos numeros do 0 ao 9
    numeros="123456789" #numeros
    numero=False
    for i in contrasinal:
        for j in numeros:
            if i==j: #se encontra numero
                numero=True
                break
        if numero == True:
            break

    return numero

print(validacion_numeros("Contrasinal1"))

def validacion_caracteres(contrasinal): #funciona igual que os 2 exercicios anteriores pero con unha cadea cos caracteres especiais
    caracteres="!@#$%&*_."
    car_especial=False
    for i in contrasinal:
        for j in caracteres:
            if i==j: #se hai caracter especial
                car_especial=True
                break
        if car_especial==True:
            break

    return car_especial

print(validacion_caracteres("Contrasinal1."))

def agregar_usuario(lista):
    bucle = True #variable para controlar o bucle
    valido = True #se é valido
    while bucle==True: #si é correcta
        print('Escribe "" para saír.')
        usuario=str(input("Introduce nombre de usuario: "))
        if usuario == "": #para sír do bucle
            bucle=False
            continue #volve ao while pero non entra polo cambio da variable bucle
        contrasinal=str(input("Introduce contrasinal: "))

        #uso as funcións do exercicio anterior para verificar o contrasinal
        if longitud_contrasenha(contrasinal) != True:
            print("Introduce 8 caracteres ao menos no contrasinal, volve a intentarlo.")
            valido = False
        
        if validacion_maiuscula(contrasinal) != True:
            print("Falta maiuscula no contrasinal, volve a intentalo.")
            valido = False

        if validacion_caracteres(contrasinal) != True:
            print("Falta caracter especial no contrasinal, volve a intentalo.")
            valido = False

        if validacion_numeros(contrasinal) != True:
            print("Falta número no contrasinal, volve a intentalo.")
            valido = False

        if valido == True: #se nunca entrou nos ifs anteriores
            lista.append([usuario, contrasinal]) #agrega o usuario á lista


    return valido #devolve se e válido ou non


print(agregar_usuario(usuarios)) #chama a función pasandolle a lista do 1er exercicio
print(usuarios)

