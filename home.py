import gestionCitas
import gestionVeterinarios
import gestionPacientes
import os
if __name__ == "__main__":
    isActivate = True
    dataClientes={'data':[]}
    dataVeterinarios={'data':[]}
    dataCitas={'data':[]}
    while isActivate:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^20}{}{:^24}|".format(' ','Menu Pricipal',' '))
        print('+','-'*55,'+')
        print("1. Gestion de Pacientes")
        print("2. Gestion de Veterinarios")
        print("3. Gestion de Citas médicas")
        print("4. Terminar")
        opcion = int(input(":)_"))
        if (opcion == 1):
            gestionPacientes.LoadInfoPaciente()
            gestionPacientes.MainMenu()
        elif (opcion == 2):
            pass
        elif (opcion == 3):
            pass
        elif (opcion == 4):
            isActivate = False
        else:
            print("Opcion no valida....")
            os.system("pause")
