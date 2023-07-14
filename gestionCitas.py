import core
import os
import agendarCitas
import gestionVeterinarios
import gestionPacientes

diccCitas = {"data":[]}

def LoadInfoCitas():
    global diccCitas
    if (core.checkFile("citas.json")):
        diccCitas = core.LoadInfo("citas.json")
    else:
        core.crearInfo("citas.json",diccCitas)

def MainMenu():
    os.system("clear")
    isPacRun = True
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE CITAS',' '))
    print('+','-'*55,'+')
    print("1. Agendar cita")
    print("2. Buscar cita")
    print("3. mostrar info")
    print("4. Regresar menu principal")
    opcion =int(input(":)_"))
    
    
    if (opcion == 1):
        paciente = input('Ingrese nombre del paciente :').upper()
        veterinario = input('Ingrese nombre del veterinario :').upper()
        
        
            print(i)
        #agendarCitas.agendarCita(paciente, veterinario)
            input(":")