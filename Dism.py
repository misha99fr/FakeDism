print("Cистема DISM\nВерсия: 10.0.22621.1")                                                                

user_input = input("\nC:\windows\system32\ ")
if user_input == "dism /Apply-Image /ImageFile:install.wim /Index:5 /ApplyDir :D:":
    print("Применение образа")
else:
	print("не является внутренней или внешней\nкомандой, исполняемой программой или пакетным файлом.")
	exit()
import time

def progress_bar():
    total = 100
    for i in range(total + 1):
        progress = "=" * i + "-" * (total - i)
        print(f"[{progress}] {i}", end="\r")
        time.sleep(0.5)

progress_bar()
print("\nОперация успешно завершена")
user_input = input("\nC:\windows\system32\ ")
if user_input == "Dism /set {default} path \Windows\System32\winload.efi":
    print("Выполнение операции")
else:
	print("не является внутренней или внешней\nкомандой, исполняемой программой или пакетным файлом.")
print("\nСоздание загрузочного раздела")
def progress_bar2():
    total = 10
    for i in range(total + 1):
        progress = "=" * i + "-" * (total - i)
        print(f"[{progress}] {i}/{total}", end="\r")
        time.sleep(0.5)
progress_bar2()
print("\nОперация завершена")
user_input = input("\nС:\windows\system32\ ")
if user_input == "exit":
 exit()
print("Выход из Dism")                                                                
