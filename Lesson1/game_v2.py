"""
Игра угадай число
Компьютер играет сам с собой
"""

import numpy as np

#number = np.random.randint(1, 101)


def random_predict(number: int=1) -> int:
    """Находит загаданное число рандомно

    Args:
        number (int, optional): Число которое нужно угадать. Defaults to 1.

    Returns:
        int: Кол-во попыток
    """
    count = 0 # Кол-во попыток
        
    while True:
        count += 1
        
        predict_number = np.random.randint(1, 101)
        
        if predict_number == number:
            break
    
    return count


def low_hight_predict(number: int=1) -> int:
    """Находит загаданное число по алгоритму границ

    Args:
        number (int, optional): Число которое нужно угадать. Defaults to 1.

    Returns:
        int: Кол-во попыток
    """
    # Границы поиска
    low = 1
    hight = 100
    
    count = 0 # Кол-во попыток
        
    while True:
        count += 1
        
        predict_number = np.random.randint(low, hight+1)
        
        if predict_number > number:
            hight = predict_number
        elif predict_number < number:
            low = predict_number
        else:
            break
    
    return count


def smard_low_hight_predict(number: int=1) -> int:
    """Находит загаданное число по алгоритму границ деля его попалам

    Args:
        number (int, optional): Число которое нужно угадать. Defaults to 1.

    Returns:
        int: Кол-во попыток
    """
    # Границы поиска
    low = 1
    hight = 100
    
    count = 0 # Кол-во попыток
    
    while True:
        count += 1
        
        predict_number = low + (hight - low) // 2
        
        if predict_number > number:
            hight = predict_number - 1
        elif predict_number < number:
            low = predict_number + 1
        else:
            break
    #print(count)
    
    return count


def score_game(predict) -> int:
    """Находит среднее число угадываний из 1000 угадываний

    Args:
        predict (_type_): Функция для угадывания числа

    Returns:
        int: Среднее число угадываний
    """
    
    count_list = []
    
    np.random.seed(1)
    random_array = np.random.randint(1, 101, 1000)
    
    for number in random_array:
        count_list.append(predict(number))
    
    score = int(np.mean(count_list))
    
    return score
    
if __name__ == "__main__":
    print(f"Среднее число угадываний алгоритма {random_predict.__name__}: {score_game(random_predict)} попыток")
    print(f"Среднее число угадываний алгоритма {low_hight_predict.__name__}: {score_game(low_hight_predict)} попыток")
    print(f"Среднее число угадываний алгоритма {smard_low_hight_predict.__name__}: {score_game(smard_low_hight_predict)} попыток")