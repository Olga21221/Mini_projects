answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом",
     "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
     "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
     "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
     "Перспективы не очень хорошие", "Весьма сомнительно"]

import random

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Назови свое имя: ')
def name():
     name = input()
     if name:
          print("Привет,", name.title())
     else:
          print('Привет')


def answer():
     while True:
          print('Задай вопрос и получишь ответ!')
          question = input()
          print(random.choice(answers))
          print('Если хочешь задать еще вопрос - напиши "Да"')
          continuation = input()
          c = ['Да', 'да', 'ДА', 'дА']
          if continuation not in c:
               print('Возвращайся если возникнут вопросы!')
               break


name()
answer()