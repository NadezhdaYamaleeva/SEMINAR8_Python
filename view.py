def show_menu():
    print(f"Выберите действие"
        "\n 1 - Показать всех сотрудников" 
        "\n 2 - Добавить сотрудника" 
        "\n 3 - Удалить сотрудника"
        "\n 4 - Выход")
    select = int(input())
    return select

def add_menu():
    print(f"Введите Фамилия Имя Номер телефона через пробел")
    man = input().split()
    return man

def delete_menu():
    print(f"Введите номер записи для удаления")
    delete = int(input())
    return delete

def show_result(msg):
    print(msg)

def show_people(people):
    for i, p in enumerate(people):
        print(i, *p, sep = "\t")