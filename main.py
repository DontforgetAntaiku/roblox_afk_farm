import pyautogui, keyboard, time, os, shelve
from threading import Thread

active = False
#Клавиши которые должны нажиматься
forward_True = ['w', 'd', 's', 'd', 'w']
forward_False =['s', 'a', 'w', 'a', 's']

forward = True
#shelve нужен потому что нажатия клавиш для библиотеки keyboard нужно предварительно записать
#Содержимое shelve
#record1=[KeyboardEvent(w down), KeyboardEvent(w up), KeyboardEvent(d down), KeyboardEvent(d up), KeyboardEvent(s down), KeyboardEvent(s up), KeyboardEvent(d down), KeyboardEvent(d up), KeyboardEvent(w down), KeyboardEvent(w up)]
#record2=[KeyboardEvent(s down), KeyboardEvent(s up), KeyboardEvent(a down), KeyboardEvent(a up), KeyboardEvent(w down), KeyboardEvent(w up), KeyboardEvent(a down), KeyboardEvent(a up), KeyboardEvent(s down), KeyboardEvent(s up)]
shelve_open = shelve.open('1', 'c')


def turinig_on():
	'''
	Функция переключает True/False (работает)
	'''
	global active
	if active == False:
		active = True
		print(active)
	else:
		active = False
		print(active)


#Вариант нажатий клавиш на клавиатуре с pyautogui, поставить на паузу с этой библиотекой гараздо тяжелее
# def snake_walk():
# 	'''
# 	Функция имитирует нажатия w,a,s,d при условии что переменная active == True
# 	'''
#     global forward
#     while active:
#         if forward:
#             for i in forward_True:
#             	pyautogui.keyDown(i)
#             	time.sleep(0.5)
#             	pyautogui.keyUp(i)
#             forward=False
#         elif not forward:
#             for i in forward_False:
#             	pyautogui.keyDown(i)
#             	time.sleep(0.5)
#             	pyautogui.keyUp(i)
#             forward = True
#         break
#     time.sleep(1)
#     snake_walk()


#Вариант нажатий клавиш на клавиатуре с keyboard, а с этой поставить на паузу легко
def snake_walk():
	'''
	Функция имитирует нажатия w,a,s,d при условии что переменная active == True
	'''
	global forward
	while active:
		if forward:
			keyboard.play(shelve_open["record1"])
			forward=False
		elif not forward:
			keyboard.play(shelve_open["record2"])
			forward = True
		break
	time.sleep(1)
	snake_walk()


def cliking():
	'''
	Функция имитирует нажатия на левую кнопку мыши пока active == True (работает)
	'''
	while active:
		pyautogui.click(button="left", clicks = 2)
		break
	time.sleep(0.5)
	cliking()


def main():
	global clicks, walking
	clicks = Thread(target=cliking)
	clicks.start()
	walking = Thread(target=snake_walk)
	walking.start()
	#Потоки нужны для того что бы и нажатия клавиш, и нажатия на ЛКМ работали вместе
	keyboard.add_hotkey('ctrl+home', turinig_on)                           #Переключение active True/False
	keyboard.add_hotkey('ctrl+end', lambda: os._exit(1))                   #Выход из программы хоткеем
	keyboard.wait('ctrl+shift+end')										   #Ожидание хоткеев


if __name__ == "__main__":
	main()