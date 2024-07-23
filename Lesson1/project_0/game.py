"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101)

# кол-во попыток
count = 0

while True:
    count += 1
    
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    if predict_number > number:
        print("Загаданное число меньше!")
    elif predict_number < number:
        print("Загаданное число больше!")
    else:
        print(f"Да! Это число {number}, ты угадал")
        print(f"Кол-во попыток: {count}")
        break