import os

inviteList = []
menu = ("1. Пригласить", "2. Удалить", "3. Вывести список", "4. Выйти")

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    for item in menu:
        print(item)

    choise = input("Действие: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if choise == '1':
        name = input("Введите имя приглашённого: ").capitalize()
        inviteList.append(name)
    elif choise == '2':
        name = input("Введите имя того, кого хотите удалить: ").capitalize()
        inviteList.remove(name)
    elif choise == '3':
        for name in inviteList:
            print(name)
        choise = input()
    elif choise == '4':
        break
    os.system('cls' if os.name == 'nt' else 'clear')
