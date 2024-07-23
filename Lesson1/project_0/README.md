# Проект 0. Игра: угадай число

Ссылка на Google Диск: https://colab.research.google.com/drive/1vQT8l55qMXpqyvr6TSgMLNjTaqaii4ps?usp=sharing

## Оглавление
[1. Описание проекта](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Какой-кейс-решаем?)

[3. Краткая информация о данных](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Этапы-работы-над-проектом)

[5. Результат](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Результат)

[6. Выводы](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Выводы)

### Описание проекта
Угадать загаданное компьютером число за минимальное число попыток

:arrow_up: [к оглавлению](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Оглавление)
___

### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток

#### Условия задания:
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать» подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше или меньше случайное число нужного нам числа.
- Представлен шаблон baseline из скринкаста.

#### Метрика качества
Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток.

#### Что практикуем
- Учимся писать хороший код на Python
- Учимся работать с IDE.
- Учимся работать с GitHub.

:arrow_up: [к оглавлению](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Оглавление)
___

### Краткая информация о данных
#### Функции
1. `random_predict` - бесконечно генерирует рандомные числа в пределах от 1 до 100 пока не наткнётся на искомое.

2. `low_hight_predict` - так же бесконечно генерирует числа, но границы поиска изменяются от `low` до `hight`, где `low = predict_number` если `number > predict_number` и `hight = predict_number` если `number < predict_number`.

`number` - искомое число.

`predict_number` - сгенерированное компьютером.

3. `smard_low_hight_predict` - предполагает, что искомое число всегда находится между между `low` и `hight`.

Каждая из функций возвращает кол-во попыток.

:arrow_up: [к оглавлению](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Оглавление)
___

### Этапы работы над проектом
Были описаны выше сказанные [функции](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Краткая-информация-о-данных) и написана программа для проведения эксперимента:

- `score_game`

Которая генерирует  1000 случайных чисел, после чего прогоняет каждое через [функции](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Краткая-информация-о-данных), и считает среднее число попыток.

:arrow_up: [к оглавлению](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Оглавление)
___

### Результат

#### В результате работы программы было выявлено:
- алгоритм рандомного поиска числа в среднем отгадывает за 101 попытку
- алгоритм границ (все еще рандомный поиск) отгадывает за 9 попыток
- алгоритм поиска среднего между двумя границами отгадывает за 5 попыток


:arrow_up: [к оглавлению](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Оглавление)
___

### Выводы
Наиболее быстрый алгоритм мне удалось реализовать с помощью поиска среднего числа между двумя границами. Данный алгоритм работает в 20 раз быстрее чем поиск рандомным способом, и в 2 раза быстрее чем поиск рандомного числа между границами отгаданных.

:arrow_up: [к оглавлению](https://github.com/GOopH4201/lessons-repo/tree/main/Lesson1/project_0/README.md#Оглавление)
___