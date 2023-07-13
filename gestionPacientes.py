import core
import os
diccPaciente = {"data":[]}

def LoadInfoPaciente():
    global diccPaciente
    if (core.checkFile("pacientes.json")):
        diccPaciente = core.LoadInfo("pacientes.json")
    else:
        core.crearInfo("pacientes.json",diccPaciente)

def MainMenu():
    os.system("clear")
    isPacRun = True
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE PACIENTES',' '))
    print('+','-'*55,'+')
    print("1. Registrar paciente")
    print("2. Buscar paciente")
    print("3. mostrar info")
    print("4. Regresar menu principal")
    opcion =int(input(":)_"))
    
    if (opcion == 1):
        os.system('clear')
        if (len(diccPaciente['data'])) == 0:
            id = 1
        else:
            id = diccPaciente['data'][-1]['id'] + 1
        
        tipos = ['Perro','Gato','Reptil','Ave']
        perros = ['Pitbull', 'Doberman', 'Pincher']
        gatos = ['Angora', 'Persa', 'Siames']
        reptiles = ['Iguana', 'Camaleon', 'Serpiente']
        aves = ['Loro', 'Perico', 'Canario']

        
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','TIPO DE MASCOTA',' '))
        print('+','-'*55,'+')
        for i, item in enumerate(tipos):
            print(f'{i+1}. {item}')
        tipo =int(input(":)_"))
        
        if (tipo == 1):
            os.system('clear')
            print('+','-'*55,'+')
            print("|{:^16}{}{:^15}|".format(' ','RAZA O ESPECIE',' '))
            print('+','-'*55,'+')
            for i, item in enumerate(perros):
                print(f'{i+1}. {item}')
            raza =int(input(":)_"))
            razas = perros
        elif (tipo == 2):
            os.system('clear')
            print('+','-'*55,'+')
            print("|{:^16}{}{:^15}|".format(' ','RAZA O ESPECIE',' '))
            print('+','-'*55,'+')
            for i, item in enumerate(gatos):
                print(f'{i+1}. {item}')
            raza =int(input(":)_"))
            razas = gatos
        elif (tipo == 3):
            os.system('clear')
            print('+','-'*55,'+')
            print("|{:^16}{}{:^15}|".format(' ','RAZA O ESPECIE',' '))
            print('+','-'*55,'+')
            for i, item in enumerate(reptiles):
                print(f'{i+1}. {item}')
            raza =int(input(":)_"))
            razas = reptiles
        elif (tipo == 4):
            os.system('clear')
            print('+','-'*55,'+')
            print("|{:^16}{}{:^15}|".format(' ','RAZA O ESPECIE',' '))
            print('+','-'*55,'+')
            for i, item in enumerate(aves):
                print(f'{i+1}. {item}')
            raza =int(input(":)_"))
            razas = aves

        data ={
            "id": id,
            "nombre":input("Ingrese el Nombre del paciente :"),
            "tipo": tipos[tipo-1],
            "raza": razas[raza-1],
            "edad":input("Ingrese la edad del paciente :"),
            "nombre":input("Ingrese el Nombre del propietario :"),
        }
        diccPaciente["data"].append(data)
        core.crearInfo("pacientes.json",data)
        
    elif (opcion == 2):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE PACIENTES',' '))
        print('+','-'*49,'+')
        print("1. Buscar por nombre")
        print("2. Buscar por tipo")
        print("3. Buscar por raza")
        print("4. Regresar gestion pacientes")
        op =int(input(":)_"))
        if (op == 1):
            pacSearch = input("Ingrese el nombre del paciente a buscar:")
            for i,item in enumerate(diccPaciente["data"]):
                if pacSearch == item["nombre"]:
                    print(f'Id paciente : {item["id"]}')
                    print(f'Nombre paciente : {item["nombre"].upper()}')
        elif (op == 2):
            pacSearch = input("Ingrese el tipo del paciente a buscar:")
            for i,item in enumerate(diccPaciente["data"]):
                if pacSearch == item["tipo"]:
                    print(f'Id paciente : {item["id"]}')
                    print(f'Nombre paciente : {item["nombre"].upper()}')
        elif (op == 3):
            pacSearch = input("Ingrese la raza del paciente a buscar:")
            for i,item in enumerate(diccPaciente["data"]):
                if pacSearch == item["raza"]:
                    print(f'Id paciente : {item["id"]}')
                    print(f'Nombre paciente : {item["nombre"].upper()}')
        
        
        input('Puse tecla para continuar: ')
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        isPacRun = False
    if (isPacRun):
        MainMenu()

    