class Animal:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f'{self.name} ест.')


class Bird(Animal):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def make_sound(self):
        return 'Chirping!'


class Mammal(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return 'Roar!'


class Reptile(Animal):
    def __init__(self, name, age, kol_limbs):
        super().__init__(name, age)
        self.kol_limbs = kol_limbs

    def make_sound(self):
        return 'Hiss!'

#Полиморфизм
def animal_sound(animals):
    for animal in animals:
        print(f'{animal.name} издает {animal.make_sound()}')


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'Добавлен {animal.name}')

    def add_staff(self, staff_name):
        self.staff.append(staff_name)
        print(f'Добавлен сотрудник {staff_name}')

    def show(self):
        for animal in self.animals:
            print(f'Животное - {animal.name}. Возраст - {animal.age}')

class Staf:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staf):
    def feel(self, animal):
        print(f'{self.name} кормит {animal.name}')

class Veterinarian(Staf):
    def doctor(self, animal):
        print(f'{self.name} лечит {animal.name}')


animals = [Bird("Ворона", 2, size = "Средняя"), Mammal("Мурка", 2, color="Белая"), Reptile("Змея", 1, kol_limbs = 0)]
animal_sound(animals)

if __name__ == "__main__":
    parrot = Bird("Попугай", 2, "Маленький")
    lion = Mammal("Лев", 5, "Коричневый")
    snake = Reptile("Змея", 3, 0)

    animal_sound([parrot, lion, snake])

    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    keeper = ZooKeeper("Виктор Андреевич")
    vet = Veterinarian("Николай Сергеевич")
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    zoo.show()
