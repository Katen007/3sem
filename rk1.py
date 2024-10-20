
class HardDisk:
    """Жесткий диск"""
    def __init__(self, id, capacity, computer_id):
        self.id = id
        self.capacity = capacity
        self.computer_id = computer_id
class Computer:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class HardDiskComputer:
    """
    'Жесткие диски в компьютере' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, computer_id, hard_disk_id, count):
        self.computer_id = computer_id
        self.hard_disk_id = hard_disk_id
        self.count = count


computers = [
    Computer(1, 'Рабочая станция'),
    Computer(2, 'Сервер'),
    Computer(3, 'Ноутбук'),
    Computer(4, 'Планшет'),
    Computer(5, 'Смартфон'),
    Computer(6, 'Игровая консоль'),
]

# Жесткие диски
hard_disks = [
    HardDisk(1, '1 ТБ', 1),
    HardDisk(2, '2 ТБ', 1),
    HardDisk(3, '500 ГБ', 2),
    HardDisk(4, '1 ТБ', 2),
    HardDisk(5, '128 ГБ', 3),
    HardDisk(6, '256 ГБ', 3),
    HardDisk(7, '64 ГБ', 4),
    HardDisk(8, '128 ГБ', 4),
    HardDisk(9, '16 ГБ', 5),
    HardDisk(10, '32 ГБ', 5),
]

# Связь жестких дисков и компьютеров
hard_disks_computers = [
    HardDiskComputer(1, 1, 2),
    HardDiskComputer(1, 2, 1),
    HardDiskComputer(2, 3, 1),
    HardDiskComputer(2, 4, 2),
    HardDiskComputer(3, 5, 1),
    HardDiskComputer(3, 6, 1),
    HardDiskComputer(4, 7, 1),
    HardDiskComputer(4, 8, 1),
    HardDiskComputer(5, 9, 1),
    HardDiskComputer(5, 10, 1),
    HardDiskComputer(2, 1, 3),
    HardDiskComputer(3, 2, 2),
    HardDiskComputer(4, 3, 1),
    HardDiskComputer(5, 4, 1),
    HardDiskComputer(6, 5, 2),
    HardDiskComputer(6, 6, 3),
    HardDiskComputer(1, 7, 2),
    HardDiskComputer(3, 8, 1),
    HardDiskComputer(2, 9, 1),
    HardDiskComputer(1, 10, 3),
]
def main():
    """Основная функция"""
# Соединение данных один-ко-многим
    one_to_many = [(hd.capacity, hd.computer_id, c.name) 
    for c in computers 
    for hd in hard_disks 
    if hd.computer_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(comp.name, hc.computer_id, hc.hard_disk_id) 
        for comp in computers 
        for hc in hard_disks_computers 
        if comp.id == hc.computer_id]

    many_to_many = [(hd.capacity, hd.computer_id, comp_name) 
        for comp_name, comp_id, hd_id in many_to_many_temp
        for hd in hard_disks if hd.id == hd_id]


    #B1
    #«Компьютер» и «Жесткий диск» связаны соотношением один-ко-многим. 
    #Выведите список всех жестких дисков, у которых емкость начинается с цифры «1», 
    #и названия их компьютеров.

    print('Задание В1')
    result = [item for item in one_to_many if item[0].startswith('1')]
    for i in result:
        print(i[0],i[2])


    #B2
    #«Компьютер» и «Жесткий диск» связаны соотношением один-ко-многим. 
    #Выведите список компьютеров с минимальной емкостью жесткого диска в каждом компьютере, 
    #отсортированный по минимальной емкости.

    print('nЗадание В2')
    min_capacities = {}
    for capacity, computer_id, comp_name in one_to_many:
        if comp_name not in min_capacities or capacity < min_capacities[comp_name]:
            min_capacities[comp_name] = capacity
    sorted_comps = sorted(min_capacities.items(), key=lambda x: x[1])
    for comp_name, capacity in sorted_comps:
        print(f"Компьютер: {comp_name}, Емкость самого маленького диска: {capacity}")


    #B3
    #«Компьютер» и «Жесткий диск» связаны соотношением многие-ко-многим. 
    #Выведите список всех связанных жестких дисков и компьютеров, отсортированный по жестким дискам, 
    #сортировка по компьютерам произвольная. 
        
    print('nЗадание В3')
    sorted_hard_disks = sorted(many_to_many, key=lambda x: (x[0], x[1]))
    for hard_disk in sorted_hard_disks:
        print(hard_disk[0],hard_disk[2])

if __name__ == '__main__':
    main()
    
