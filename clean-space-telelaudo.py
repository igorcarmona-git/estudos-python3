# O código abaixo verifica pelos arquivos no Disco C do servidor do Telelaudo, se o espaço em disco for menor do que 5GB ele realiza as exclusões das pastas não atuais

import os
import shutil
import datetime

base_dir = r'C:\dcm4chee\dcm4chee-2.18.0-psql\server\default\archive\DCM4CHEE'
current_year = str(datetime.datetime.now().year)
current_month = str(datetime.datetime.now().month)
current_day = str(datetime.datetime.now().day)
current_date = datetime.datetime.now()

# Verifica se o disco local C tem menos de 5GB de espaço livre
c_drive = os.getenv('SystemDrive')
total, used, free = shutil.disk_usage(c_drive)

# Convertendo bytes para gigabytes
totalGB = total / (1024 ** 3)
totalGB_formated = float("{:.2f}".format(totalGB))

usedGB = used / (1024 ** 3)
usedGB_formated = float("{:.2f}".format(usedGB))

freeGB = free / (1024 ** 3)
freeGB_formated = float("{:.2f}".format(freeGB))

print("Espaço total em disco:", totalGB_formated, "GB")
print("Espaço usado em disco:", usedGB_formated, "GB")
print("Espaço livre em disco:", freeGB_formated, "GB")

try:
    if freeGB_formated < 5.00:
        # Verifica e exclui pastas com ano diferente do ano atual
        for dir_name in os.listdir(base_dir):
            if dir_name != current_year:
                dir_path = os.path.join(base_dir, dir_name)
                print(f"Exclui pastas com ano diferente do ano atual")
                print(f"Deleting dir: {dir_path}...")
                shutil.rmtree(dir_path)

        # Entra na pasta do ano atual
        year_dir = os.path.join(base_dir, current_year)
        os.chdir(year_dir)
        print(year_dir)

        # Verifica e exclui pastas com mes diferente do atual
        for name_month in os.listdir(year_dir):
            if name_month != current_month:
                dir_path_month = os.path.join(year_dir, name_month)
                print(f"Exclui pastas com mes diferente do mes atual")
                print(f"Deleting dir: {dir_path_month}...")
                shutil.rmtree(dir_path_month)
            
        # Entra na pasta do mes atual
        month_dir = os.path.join(base_dir, current_year, current_month)
        os.chdir(month_dir)
        print(month_dir)

        for name_day in os.listdir(month_dir):
            if name_day != current_day:
                dir_path_day = os.path.join(month_dir, name_day)
                print(f"Exclui pastas com dias diferente do dia atual")
                print(f"Deleting dir: {dir_path_day}...")

                try:
                    shutil.rmtree(dir_path_day)
                    print(f"Deleted dir: {dir_path_day}")
                except PermissionError as e:
                    print(f"Permission error deleting dir: {dir_path_day}")
                    continue
    else:
        print(f"O espaço em disco tem mais de 5GB livres.")
except os.error as error:
    os.system('pause')
    print("Erro:", error)
