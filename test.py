number = int(input("Введите число: "))
while number != 0:
    if number % 2 == 0:
        print(f"Число {number} является четным ")
    else:
        print(f"Число {number} не является четным ")
    number = int(input("Введите число: "))

