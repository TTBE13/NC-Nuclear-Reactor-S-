import time
import random

topl = 100
val = 30
timet = 0
minpl = 'r'
e = 0
t = 0
temp = 20
e = int(input("Выбирите сложность(1-легко,2-норм,3-сложно)>>"))
if e == 1:
	i = 1
	while True:
		time.sleep(0.3)
		t = t + 2
		temp = temp + i
		val = val + 1
		topl = topl - 1
		print("температура реактора", temp, "и", topl, "% топлива")
		if t == 10:
			minpl = input("Введите 'y' чтобы понизить температуру реактора или 't' чтобы повысить температуру реактора или 'u' чтобы купить топливо>>")
			t = t - 10
		if minpl == 'y':
			i = i - 2
			print("температура реактора понижается")
		if minpl == 't':
			i = i + 2
			print("температура реактора повышается")
		if minpl == 'u':
			val = val - 5
			topl = topl + 10
			print("у тебя осталось", val, "денег и", topl, "% топлива")
			minpl = 'l'
		if topl < 1:
			print("вы проиграли, в реакторе не осталось топлива")
			break
		if temp > 1500:
			print("вы проиграли, реактор взорвался")
			break
		if temp < 0:
			print("вы проиграли, реактор выключился")
			break
if e == 2:
	i = 1
	while True:
		time.sleep(0.3)
		t = t + 3
		temp = temp + i
		val = val + 1
		topl = topl - 1
		print("температура реактора", temp, "и", topl, "% топлива")
		if t == 15:
			minpl = input("Введите 'y' чтобы понизить температуру реактора или 't' чтобы повысить температуру реактора или 'u' чтобы купить топливо>>")
			t = t - 15
		if minpl == 'y':
			i = i - 2
			print("температура реактора понижается")
		if minpl == 't':
			i = i + 2
			print("температура реактора повышается")
		if minpl == 'u':
			val = val - 5
			topl = topl + 10
			print("у тебя осталось", val, "денег и", topl, "% топлива")
			minpl = 'l'
		if topl < 1:
			print("вы проиграли, в реакторе не осталось топлива")
			break
		if temp > 1500:
			print("вы проиграли, реактор взорвался")
			break
		if temp < 0:
			print("вы проиграли, реактор выключился")
			break
if e == 3:
	i = 1
	while True:
		time.sleep(0.3)
		timet = timet + 0.3
		t = t + 2
		temp = temp + i
		val = val + 1
		topl = topl - 1
		print("температура реактора", temp, "и", topl, "% топлива")
		if t == 20:
			minpl = input("Введите 'y' чтобы понизить температуру реактора или 't' чтобы повысить температуру реактора или 'u' чтобы купить топливо>>")
			t = t - 20
		if minpl == 'y':
			i = i - 2
			print("температура реактора понижается")
		if minpl == 't':
			i = i + 2
			print("температура реактора повышается")
		if minpl == 'u':
			val = val - 5
			topl = topl + 10
			print("у тебя осталось", val, "денег и", topl, "% топлива")
			minpl = 'l'
		if timet > 60:
			print("поздравляю! ты прошёл игру!")
			break
		if topl < 1:
			print("вы проиграли, в реакторе не осталось топлива")
			break
		if temp > 1500:
			print("вы проиграли, реактор взорвался")
			break
		if temp < 0:
			print("вы проиграли, реактор выключился")
			break