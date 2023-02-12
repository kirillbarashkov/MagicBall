import random
from time import sleep

answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом",
           "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
           "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
           "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
           "Перспективы не очень хорошие", "Весьма сомнительно"]

print('Магический шар: Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос!')
sleep(0.5)
name = input('Магический шар: Скажи, как к тебе обращаться? >> ')
print('Магический шар: Привет ', name, '!', sep = '')
sleep(0.5)

answer = 'да'

while answer.lower() == 'да':
    question = input(f'Магический шар: Задай свой вопрос, {name}: >> ')
    sleep(len(question)*0.1)
    print(f'Магический шар: Мой ответ - <<<{random.choice(answers)}>>>')
    answer = input('Магический шар: Продолжим? (да/нет): ').lower().strip()
    if answer not in("да","нет"):
        print("Ошибка!!! Введите 'да' или 'нет'")
        answer = 'да'
        continue
    elif answer == 'да':
        answer = 'да'
    elif answer == 'нет':
        print(f'Магический шар: {name}, возвращайся если возникнут вопросы!')
        break