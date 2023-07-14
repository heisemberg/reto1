import core
import os
from datetime import datetime
diccVeterinario = {"data":[]}

def LoadInfoveterinario():
    global diccVeterinario
    if (core.checkFile("veterinarios.json")):
        diccVeterinario = core.LoadInfo("veterinarios.json")
    else:
        core.crearInfo("veterinarios.json",diccVeterinario)

def MainMenu():
    os.system("clear")
    isVetRun = True
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE VETERINARIOS',' '))
    print('+','-'*55,'+')
    print("1. Registrar veterinario")
    print("2. Buscar veterinario")
    print("3. mostrar info")
    print("4. Regresar menu principal")
    opcion =int(input(":)_"))
    
    if (opcion == 1):
        os.system('clear')
        id = input('Ingrese el ID del veterinario :')
        especialidades = ['Traumatologia','Dermatologia','Oftalmologia','Fisioterapia','Anestesiologia','Cardilogo', 'Neurologia']
        
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','ESPECIALIDAD DEL VETERINARIO',' '))
        print('+','-'*55,'+')
        for i, item in enumerate(especialidades):
            print(f'{i+1}. {item}')
        espe =int(input(":)"))
        esp = especialidades[espe-1]
        
        data ={
            "id": id,
            "nombre":input("Ingrese el Nombre del veterinario :").upper(),
            "especialidad": esp.upper(),
            "edad":input("Ingrese la edad del veterinario :"),
            "fecha": str(datetime.now()),
            "agenda": []
        }
        diccVeterinario['data'].append(data)
        core.crearInfo("veterinarios.json",data)
        
    elif (opcion == 2):
        search = True
        while search:
            os.system("clear")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE VETERINARIOS',' '))
            print('+','-'*49,'+')
            print("1. Buscar por nombre")
            print("2. Buscar por especialidad")
            print("3. Regresar gestion veterinarios")
            op =int(input(":)_"))
        
            if (op == 1):
                vetSearch = input("Ingrese el nombre del veterinario a buscar:").upper()
                for i,item in enumerate(diccVeterinario['data']):
                    if vetSearch == item["nombre"]:
                        print(f'Id veterinario : {item["id"]}')
                        print(f'Nombre veterinario : {item["nombre"].upper()}')
            elif (op == 2):
                vetSearch = input("Ingrese la especialidad del veterinario a buscar:").upper()
                for i,item in enumerate(diccVeterinario['data']):
                    if vetSearch == item["especialidad"]:
                        print(f'Id veterinario : {item["id"]}')
                        print(f'Nombre veterinario : {item["nombre"].upper()}')

            search=bool(input("Si desea buscar otro veterinario puse 'S', de lo contrario pulse enter para salir: "))
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        isVetRun = False
    if (isVetRun):
        MainMenu()

    