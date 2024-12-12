
import unittest

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

class TestHardDisk(unittest.TestCase):
    def test_hard_disk_init(self):
        hard_disk = HardDisk(1, "1TB", 1)
        self.assertEqual(hard_disk.id, 1)
        self.assertEqual(hard_disk.capacity, "1TB")
        self.assertEqual(hard_disk.computer_id, 1)
class TestComputer(unittest.TestCase):
    def test_computer_init(self):
        computer = Computer(1, "Workstation")
        self.assertEqual(computer.id, 1)
        self.assertEqual(computer.name, "Workstation")

class TestHardDiskComputer(unittest.TestCase):
    def test_hard_disk_computer_init(self):
        hard_disk_computer = HardDiskComputer(1, 1, 2)
        self.assertEqual(hard_disk_computer.computer_id, 1)
        self.assertEqual(hard_disk_computer.hard_disk_id, 1)
        self.assertEqual(hard_disk_computer.count, 2)



if __name__ == '__main__':
    unittest.main()
