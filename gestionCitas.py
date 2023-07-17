import core
import os
from datetime import datetime
from datetime import timedelta

diccCitas = {"data":[]}

if (core.checkFile("veterinarios.json")):
        diccVeterinario = core.LoadInfo("veterinarios.json")
if (core.checkFile("pacientes.json")):
        diccPaciente = core.LoadInfo("pacientes.json")

def LoadInfoCitas():
    global diccCitas
    if (core.checkFile("citas.json")):
        diccCitas = core.LoadInfo("citas.json")
    else:
        core.crearInfo("citas.json",diccCitas)


def MainMenu():
    os.system("clear")
    isCitRun = True
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE CITAS',' '))
    print('+','-'*55,'+')
    print("1. Agendar cita")
    print("2. Buscar cita")
    print("3. mostrar info")
    print("4. Regresar menu principal")
    opcion =int(input(":)_"))
    
    if (opcion == 1):
        search = True
        if (len(diccCitas['data'])) == 0:
            id = 1
        else:
            id = diccCitas['data'][-1]['id'] + 1

        paciente = input('Ingrese nombre del paciente :').upper()
        for k in diccPaciente['data']:
            if paciente == k['nombre']:
                idPac = k['id']
                especialista = input('Ingrese especialidad de la cita :').upper()
                while search:
                    for i,item in enumerate(diccVeterinario['data']):
                        if especialista == item['especialidad']:
                            vetSearch = item["nombre"]
                            print(f'Id veterinario : {item["id"]}\nNombre del especialista : {item["nombre"]}')     

                            agendar = True     
                            while agendar:
                                if len(item["agenda"]) == 0:
                                    now = datetime.now()
                                    newDate = now + timedelta(days=1)
                                    horaIni = datetime(now.year, now.month , newDate.day , 8, 00, 00, 00000)
                                    horaSal = datetime(now.year, now.month , newDate.day , 17, 00, 00, 00000)
                                    horaIniAlm = datetime(now.year, now.month , newDate.day , 11, 00, 00, 00000)
                                else:
                                    horaIni = datetime.strptime(item["agenda"][-1],'%Y-%m-%d %H:%M:%S')
                                    horaSal = datetime(horaIni.year, horaIni.month , horaIni.day , 17, 00, 00, 00000)
                                    horaIniAlm = datetime(horaIni.year, horaIni.month , horaIni.day , 11, 00, 00, 00000)
                                if horaIni < horaSal:
                                    if str(horaIni) in item["agenda"]:
                                        if horaIni == horaIniAlm:
                                            horaIni = horaIni + timedelta(hours=3)
                                            data ={
                                                "id": id,
                                                "fecha": str(horaIni),
                                                "nombreVet": vetSearch,
                                                "especialidad": especialista,
                                                "paciente": paciente,
                                                "idPac": idPac
                                                }

                                            item["agenda"].append(str(horaIni))
                                            core.EditarData("veterinarios.json",diccVeterinario)
                                            diccCitas['data'].append(data)
                                            core.EditarData("citas.json",diccCitas)
                                            agendar=bool(input("Pulse enter para continuar: "))
                                        else:
                                            horaIni = horaIni + timedelta(hours=1)
                                            data ={
                                                "id": id,
                                                "fecha": str(horaIni),
                                                "nombreVet": vetSearch,
                                                "especialidad": especialista,
                                                "paciente": paciente,
                                                "idPac": idPac
                                                }
                                            diccCitas['data'].append(data)
                                            core.EditarData("citas.json",diccCitas)
                                            item["agenda"].append(str(horaIni))
                                            core.EditarData("veterinarios.json",diccVeterinario)
                                            agendar=bool(input("Pulse enter para continuar: "))
                                    else:
                                        data ={
                                            "id": id,
                                            "fecha": str(horaIni),
                                            "nombreVet": vetSearch,
                                            "especialidad": especialista,
                                            "paciente": paciente,
                                            "idPac": idPac
                                            }
                                        diccCitas['data'].append(data)
                                        core.EditarData("citas.json",diccCitas)
                                        item["agenda"].append(str(horaIni))
                                        core.EditarData("veterinarios.json",diccVeterinario)
                                        agendar=bool(input("Pulse enter para continuar: "))
                                else:
                                    horaIni = horaIni + timedelta(days=1,hours=-9)
                                    horaSal = horaSal + timedelta(days=1)
                                    horaIniAlm = horaIniAlm + timedelta(days=1)
                                    data ={
                                        "id": id,
                                        "fecha": str(horaIni),
                                        "nombreVet": vetSearch,
                                        "especialidad": especialista,
                                        "paciente": paciente,
                                        "idPac": idPac
                                        }
                                    diccCitas['data'].append(data)
                                    core.EditarData("citas.json",diccCitas)
                                    item["agenda"].append(str(horaIni))
                                    core.EditarData("veterinarios.json",diccVeterinario)
                                    agendar=bool(input("Pulse enter para continuar: "))
                                print(f'La cita quedo agendada para {item["agenda"][-1]}')
                                agendar= False

                    search=bool(input("Pulse enter para salir: "))
                

    elif (opcion == 4):
            isCitRun = False
    if (isCitRun):
        MainMenu()