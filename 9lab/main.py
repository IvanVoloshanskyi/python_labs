from employee import Worker
from manager import Manager
from scientist import Scientist
from workman import WorkingMan
from brigadier import Brigadier


def main():
    print("==========================================")
    manager = Manager("John", 40, "Manager", 12, 40000, "PrivatBank")
    print(manager)

    print("==========================================")
    scientist = Scientist("William", 45, "Scientist-Doctor", 17, 50000, "cancer medicine")
    print(scientist)

    print("==========================================")
    workman = WorkingMan("Peter", 18, "Builder", 0.5, 25000, 112)
    print(workman)

    print("==========================================")
    brigadier = Brigadier("Stepan", 38, "Brigadier", 12, 35000, 5)
    print(brigadier)


if __name__ == '__main__':
    main()
