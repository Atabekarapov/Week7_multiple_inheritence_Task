# TASK1. WEEK7. ATABEK
# 1)
'''Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с
методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник.'''
import datetime

# class Clock:
#     def show_time(self):
#         print(datetime.datetime.now())
# class Alarm:
    
#     def clock_turn_on(self):
#         print("Thank you, alarm clock is turned on!")

#     def clock_turn_off(self):
#         print("Thank you, alarm clock is turned off!")

# class AlarmClock(Clock, Alarm):

#     def put_alarm_clock(self):
#         print(datetime.time(int(input("Can you please put the AlarmClock: "))))
        
# ready = Clock()
# ready.show_time()
# Time = AlarmClock()
# Time.put_alarm_clock()
# Time.clock_turn_on()

# 2)
'''Напишите класс Coder с атрибутами experience, count_code_time = 0 и методами get_info и
coding (возвращает ошибку возвращает ошибку NotImplementedError). Создайте классы Backend и Frontend, которые
наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать
дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (возвращает ошибку так, чтобы он принимал количество
часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). Так
же бывают FullStack разработчики и поэтому создайте данный класс и чтобы у него были
атрибуты и методы предыдущих классов.
Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы.'''


# class Coder:
#     experience = ''
#     count_code_time = 0
    
#     def get_info(self):
#         pass

#     def coding(self):
#         pass

# class Backend(Coder):
#     """Класс для бэкенда"""

#     def init(self, languages_backend):
#         self.experience = languages_backend

#     def get_info(self):
#         print(f'Ваш язык {self.experience} ваше время кода {self.count_code_time} часов ')

#     def coding(self, time):
#         self.count_code_time += time

# class Frontend(Coder):
#     """Класс для фронтенда"""

#     def init(self, languages_frontend):
#         self.experience = languages_frontend

#     def get_info(self):
#         print(f'Ваш язык {self.experience} ваше время кода {self.count_code_time} часов ')

#     def coding(self, time):
#         self.count_code_time += time


# class FullStack(Frontend, Backend, Coder):

#     def init(self, languages_frontend):
#         self.experience = languages_frontend


# backend1 = Backend()
# backend1.coding(12)
# backend1.get_info()

# fronted1 = Frontend()
# fronted1.coding(13)
# fronted1.get_info()

# full_stack = FullStack()
# full_stack.coding(34)
# full_stack.get_info()

# 3)
'''Колода карт
Создайте класс для колоды карт. Внутри класса Deck должен использоваться другой
класс - Card.
Требования:
• Класс колоды должен иметь метод deal для раздачи одной карты из колоды.
• После раздачи карта удаляется из колоды.
• Должен быть метод mix, который гарантирует, что в колоде есть все 52 карты, а затем
перемешивает их случайным образом.
• Класс карты должен иметь масть (возвращает ошибку червы, бубны, трефы, пики) и ценность (возвращает ошибку A, 2 , 3, 4,
5, 6, 7, 8, 9, 10, J, Q, K) )
Примечание: используйте random shuffle (возвращает ошибку from random import shuffle)'''
# import random

# class deck:










# 4)
# def hackerrankInString(s):
#     target = 'hackerrank'
#     n = len(target)
    
#     i = 0
    
#     for char in s:
#         if char == target[i]:
#             i += 1
#             if i == n:
#                 return "YES"
#     return "NO"









