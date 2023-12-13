import time
import random

bio = 0.3
coal = 0.5
gas = 0.7
neft = 0.9

bioval = 200
coalval = 500
gasval = 700
neftval = 900

kolvobio = 0
kolvocoal = 0
kolvogas = 0
kolvoneft = 0

kl = 1
kli = 1
kp = 1
kpi = 1
kj = 1
kji = 1

u = 1
p = 3
t = 5
a = 7
s = 9
fh = 10

ut = 2
pt = 4
tt = 6
at = 8
st = 10
fht = 11

uval = 1.2
pval = 1.5
tval = 2.2
aval = 3.2
sval = 4.5
fhval = 6

uvalt = 1
pvalt = 5
tvalt = 9
avalt = 13
svalt = 17
fhvalt = 25

utopl = 100
ptopl = 0
ttopl = 0
atopl = 0
stopl = 0
fhtopl = 0

tip = u
tipval = uvalt

m = 'z'
l = 0
topl = 100
val = 30
timet = 0
timet2 = 0
minpl = 'r'
e = 0
t = 0
temp = 20
tiptemp = ut
e = int(input("Выбирите сложность(1-легко,2-норм,3-сложно)>>"))
if e == 1:
	val = val + 20
	u = u + 2
	p = p + 2
	t = t + 2
	a = a + 2
	i = tip
	while True:
		time.sleep(0.3)
		timet = timet + 0.3
		t = t + 2
		temp = temp + i
		val = val + tipval
		topl = topl - 1
		if kolvobio > 0:
			todar = bio * kolvobio
			val = val + todar
		if kolvocoal > 0:
			todar2 = bio * kolvocoal
			val = val + todar2
		if kolvogas > 0:
			todar3 = bio * kolvogas
			val = val + todar3
		if kolvoneft > 0:
			todar4 = bio * kolvoneft
			val = val + todar4
		print("температура реактора", temp, "и", topl, "% топлива и", val, "денег")
		if t == 10:
			val = val - 1
			if val > 500 and val < 600:
				val = val + 30
				print("поздравляю ты получил 500 денег, бонус + 30 денег, у тебя", val, "денег")
			if val > 1000 and val < 1200:
				val = val + 60
				print("поздравляю ты получил 1000 денег, бонус + 60 денег, у тебя", val, "денег")
			if val > 5000 and val < 5200:
				val = val + 100
				print("поздравляю ты получил 5000 денег, бонус + 100 денег, у тебя", val, "денег")
			if val > 10000 and val < 10200:
				val = val + 120
				print("поздравляю ты получил 10000 денег, бонус + 120 денег, у тебя", val, "денег")
			if val < -150:
				print("вы проиграли, вы потеряли все деньги и больше не можете ничего оплатить")
				break
			minpl = input("Введите 'y' чтобы понизить температуру реактора или 't' чтобы повысить температуру реактора или 'u' чтобы купить топливо или 'i' чтобы купить доп ЭС>>")
			t = t - 10
		if minpl == 'y':
			i = i - tiptemp
			print("температура реактора понижается")
		if minpl == 't':
			i = i + tiptemp
			print("температура реактора повышается")
		if minpl == 'i':
			tipes = input("Выберете тип ЭС(b-сжигатель биотоплива, c-угольная ЭС, g-газовая ЭС(недоступно), n-нефтяная ЭС(недоступно))>>")
			kolvoes = int(input("Введите колличество ЭС>>"))
			if tipes == 'b':
				kop = kolvoes * bioval
				val = val - kop
				kolvobio = kolvobio + kolvoes
				print("вы купили", kolvobio, "сжигателей биотоплива, у вас", val, "денег и", kolvobio, "сжигателей биотоплива")
				tipes = 'm'
				minpl = 'a'
			if tipes == 'c':
				kop = kolvoes * coalval
				val = val - kop
				kolvocoal = kolvocoal + kolvoes
				print("вы купили", kolvocoal, "угольных ЭС, у вас", val, "денег и", kolvocoal, "угольных ЭС")
				tipes = 'm'
				minpl = 'a'
		if minpl == 'u':
			tipt = input("Введите тип топлива(u-уран, p-плутоний, t-торий, a=америций, s-шрабидий, fh-жар огненный)>>")
			kolvo = int(input("Введите кол-во топлива>>"))
			if tipt == 'u':
				tipval = uvalt
				tip = u
				i = tip
				tiptemp = ut
				if kl == 1:
					topl = utopl
					kli = 1
					kp = 1
					kpi = 1
					kl = 0
				utopl = topl
				tipol = uval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				utopl = utopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 'p':
				tipval = pvalt
				tip = p
				i = tip
				tiptemp = pt
				if kli == 1:
					topl = ptopl
					kl = 1
					kp = 1
					kpi = 1
					kli = 0
				ptopl = topl
				tipol = pval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				ptopl = ptopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 't':
				tipval = tvalt
				tip = t
				i = tip
				tiptemp = tt
				if kp == 1:
					topl = ttopl
					kl = 1
					kli = 1
					kpi = 1
					kp = 0
				ttopl = topl
				tipol = tval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				ttopl = ttopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 'a':
				tipval = avalt
				tip = a
				i = tip
				tiptemp = at
				if kpi == 1:
					topl = atopl
					kl = 1
					kli = 1
					kp = 1
					kpi = 0
				atopl = topl
				tipol = aval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				atopl = atopl +atopl
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 's':
				tipval = svalt
				tip = s
				i = tip
				tiptemp = st
				if kj == 1:
					topl = stopl
					kl = 1
					kli = 1
					kp = 1
					kpi = 1
					kji = 1
					kj = 0
				stopl = topl
				tipol = sval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				stopl = utopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 'fh':
				tipval = fhvalt
				tip = fh
				i = tip
				tiptemp = fht
				if kji == 1:
					topl = fhtopl
					kl = 1
					kli = 1
					kp = 1
					kpi = 1
					kj = 1
					kji = 0
				fhtopl = topl
				tipol = fhval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				fhtopl = utopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
		if timet > 150:
			val = val + 150
			print("поздравляю! ты прошёл игру!")
			m =  input("Если хотите продолжить нажмите 'b' или любую другую клавишу чтобы закончить игру>>")
			if m == 'b':
				print("+ 150 денег, у вас", val, "денег")
				timet = timet - 91
			else:
				break
		if topl < 1:
			print("вы проиграли, в реакторе не осталось топлива")
			break
		if temp > 1500:
			print(" ")
			print("              *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("   *         *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("   ***")
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("  *****")
			print("   ***")
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("*******")
			print("  *****")
			print("   ***")
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.5)
			print("вы проиграли, реактор взорвался")
			break
		if temp < 0:
			print("вы проиграли, реактор выключился")
			break
if e == 2:
	val = val + 10
	u = u + 1
	p = p + 1
	t = t + 1
	a = a + 1
	i = tip
	while True:
		time.sleep(0.3)
		timet = timet + 0.3
		t = t + 3
		temp = temp + i
		val = val + tipval
		topl = topl - 1
		if kolvobio > 0:
			todar = bio * kolvobio
			val = val + todar
		if kolvocoal > 0:
			todar2 = bio * kolvocoal
			val = val + todar2
		if kolvogas > 0:
			todar3 = bio * kolvogas
			val = val + todar3
		if kolvoneft > 0:
			todar4 = bio * kolvoneft
			val = val + todar4
		print("температура реактора", temp, "и", topl, "% топлива и", val, "денег")
		if t == 21:
			val = val - 2
			if val > 500 and val < 600:
				val = val + 30
				print("поздравляю ты получил 500 денег, бонус + 30 денег, у тебя", val, "денег")
			if val > 1000 and val < 1200:
				val = val + 60
				print("поздравляю ты получил 1000 денег, бонус + 60 денег, у тебя", val, "денег")
			if val > 5000 and val < 5200:
				val = val + 100
				print("поздравляю ты получил 5000 денег, бонус + 100 денег, у тебя", val, "денег")
			if val > 10000 and val < 10200:
				val = val + 120
				print("поздравляю ты получил 10000 денег, бонус + 120 денег, у тебя", val, "денег")
			if val < -120:
				print("вы проиграли, вы потеряли все деньги и больше не можете ничего оплатить")
				break
			minpl = input("Введите 'y' чтобы понизить температуру реактора или 't' чтобы повысить температуру реактора или 'u' чтобы купить топливо или 'i' чтобы купить доп ЭС>>")
			t = t - 21
		if minpl == 'y':
			i = i - tiptemp
			print("температура реактора понижается")
		if minpl == 't':
			i = i + tiptemp
			print("температура реактора повышается")
		if minpl == 'i':
			tipes = input("Выберете тип ЭС(b-сжигатель биотоплива, c-угольная ЭС, g-газовая ЭС(недоступно), n-нефтяная ЭС(недоступно))>>")
			kolvoes = int(input("Введите колличество ЭС>>"))
			if tipes == 'b':
				kop = kolvoes * bioval
				val = val - kop
				kolvobio = kolvobio + kolvoes
				print("вы купили", kolvobio, "сжигателей биотоплива, у вас", val, "денег и", kolvobio, "сжигателей биотоплива")
				tipes = 'm'
				minpl = 'a'
			if tipes == 'c':
				kop = kolvoes * coalval
				val = val - kop
				kolvocoal = kolvocoal + kolvoes
				print("вы купили", kolvocoal, "угольных ЭС, у вас", val, "денег и", kolvocoal, "угольных ЭС")
				tipes = 'm'
				minpl = 'a'
		if minpl == 'u':
			tipt = input("Введите тип топлива(u-уран, p-плутоний, t-торий, a=америций, s-шрабидий, fh-жар огненный)>>")
			kolvo = int(input("Введите кол-во топлива>>"))
			if tipt == 'u':
				tipval = uvalt
				tip = u
				i = tip
				tiptemp = ut
				if kl == 1:
					topl = utopl
					kli = 1
					kp = 1
					kpi = 1
					kl = 0
				utopl = topl
				tipol = uval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				utopl = utopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 'p':
				tipval = pvalt
				tip = p
				i = tip
				tiptemp = pt
				if kli == 1:
					topl = ptopl
					kl = 1
					kp = 1
					kpi = 1
					kli = 0
				ptopl = topl
				tipol = pval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				ptopl = ptopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 't':
				tipval = tvalt
				tip = t
				i = tip
				tiptemp = tt
				if kp == 1:
					topl = ttopl
					kl = 1
					kli = 1
					kpi = 1
					kp = 0
				ttopl = topl
				tipol = tval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				ttopl = ttopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 'a':
				tipval = avalt
				tip = a
				i = tip
				tiptemp = at
				if kpi == 1:
					topl = atopl
					kl = 1
					kli = 1
					kp = 1
					kpi = 0
				atopl = topl
				tipol = aval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				atopl = atopl +atopl
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 's':
				tipval = svalt
				tip = s
				i = tip
				tiptemp = st
				if kj == 1:
					topl = stopl
					kl = 1
					kli = 1
					kp = 1
					kpi = 1
					kji = 1
					kj = 0
				stopl = topl
				tipol = sval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				stopl = utopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 'fh':
				tipval = fhvalt
				tip = fh
				i = tip
				tiptemp = fht
				if kji == 1:
					topl = fhtopl
					kl = 1
					kli = 1
					kp = 1
					kpi = 1
					kj = 1
					kji = 0
				fhtopl = topl
				tipol = fhval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				fhtopl = utopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
		if timet > 120:
			val = val + 200
			print("поздравляю! ты прошёл игру!")
			m =  input("Если хотите продолжить нажмите 'b' или любую другую клавишу чтобы закончить игру>>")
			if m == 'b':
				print("+ 200 денег, у вас", val, "денег")
				timet = timet - 91
			else:
				break
		if topl < 1:
			print("вы проиграли, в реакторе не осталось топлива")
			break
		if temp > 1500:
			print(" ")
			print("              *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("   *         *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("   ***")
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("  *****")
			print("   ***")
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("*******")
			print("  *****")
			print("   ***")
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.5)
			print("вы проиграли, реактор взорвался")
			break
		if temp < 0:
			print("вы проиграли, реактор выключился")
			break
if e == 3:
	i = tip
	while True:
		time.sleep(0.3)
		timet = timet + 0.3
		timet2 = timet2 + 0.3
		t = t + 2
		temp = temp + i
		val = val + tipval
		topl = topl - 1
		if kolvobio > 0:
			todar = bio * kolvobio
			val = val + todar
		if kolvocoal > 0:
			todar2 = bio * kolvocoal
			val = val + todar2
		if kolvogas > 0:
			todar3 = bio * kolvogas
			val = val + todar3
		if kolvoneft > 0:
			todar4 = bio * kolvoneft
			val = val + todar4
		print("температура реактора", temp, "и", topl, "% топлива и", val, "денег")
		if t == 20:
			val = val - 3
			if val > 500 and val < 600:
				val = val + 30
				print("поздравляю ты получил 500 денег, бонус + 30 денег, у тебя", val, "денег")
			if val > 1000 and val < 1200:
				val = val + 60
				print("поздравляю ты получил 1000 денег, бонус + 60 денег, у тебя", val, "денег")
			if val > 5000 and val < 5200:
				val = val + 100
				print("поздравляю ты получил 5000 денег, бонус + 100 денег, у тебя", val, "денег")
			if val > 10000 and val < 10200:
				val = val + 120
				print("поздравляю ты получил 10000 денег, бонус + 120 денег, у тебя", val, "денег")
			if val < -100:
				print("вы проиграли, вы потеряли все деньги и больше не можете ничего оплатить")
				break
			minpl = input("Введите 'y' чтобы понизить температуру реактора или 't' чтобы повысить температуру реактора или 'u' чтобы купить топливо или 'i' чтобы купить доп ЭС>>")
			t = t - 20
		if minpl == 'y':
			i = i - tiptemp
			print("температура реактора понижается")
		if minpl == 't':
			i = i + tiptemp
			print("температура реактора повышается")
		if minpl == 'i':
			tipes = input("Выберете тип ЭС(b-сжигатель биотоплива, c-угольная ЭС, g-газовая ЭС(недоступно), n-нефтяная ЭС(недоступно))>>")
			kolvoes = int(input("Введите колличество ЭС>>"))
			if tipes == 'b':
				kop = kolvoes * bioval
				val = val - kop
				kolvobio = kolvobio + kolvoes
				print("вы купили", kolvobio, "сжигателей биотоплива, у вас", val, "денег и", kolvobio, "сжигателей биотоплива")
				tipes = 'm'
				minpl = 'a'
			if tipes == 'c':
				kop = kolvoes * coalval
				val = val - kop
				kolvocoal = kolvocoal + kolvoes
				print("вы купили", kolvocoal, "угольных ЭС, у вас", val, "денег и", kolvocoal, "угольных ЭС")
				tipes = 'm'
				minpl = 'a'
		if minpl == 'u':
			tipt = input("Введите тип топлива(u-уран, p-плутоний, t-торий, a-америций, s-шрабидий, fh-жар огненный)>>")
			kolvo = int(input("Введите кол-во топлива>>"))
			if tipt == 'u':
				tipval = uvalt
				tip = u
				i = tip
				tiptemp = ut
				if kl == 1:
					topl = utopl
					kli = 1
					kp = 1
					kpi = 1
					kj = 1
					kji = 1
					kl = 0
				utopl = topl
				tipol = uval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				utopl = utopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 'p':
				tipval = pvalt
				tip = p
				i = tip
				tiptemp = pt
				if kli == 1:
					topl = ptopl
					kl = 1
					kp = 1
					kpi = 1
					kj = 1
					kji = 1
					kli = 0
				ptopl = topl
				tipol = pval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				ptopl = ptopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 't':
				tipval = tvalt
				tip = t
				i = tip
				tiptemp = tt
				if kp == 1:
					topl = ttopl
					kl = 1
					kli = 1
					kpi = 1
					kj = 1
					kji = 1
					kp = 0
				ttopl = topl
				tipol = tval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				ttopl = ttopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 'a':
				tipval = avalt
				tip = a
				i = tip
				tiptemp = at
				if kpi == 1:
					topl = atopl
					kl = 1
					kli = 1
					kp = 1
					kj = 1
					kji = 1
					kpi = 0
				atopl = topl
				tipol = aval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				atopl = atopl +atopl
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 's':
				tipval = svalt
				tip = s
				i = tip
				tiptemp = st
				if kj == 1:
					topl = stopl
					kl = 1
					kli = 1
					kp = 1
					kpi = 1
					kji = 1
					kj = 0
				stopl = topl
				tipol = sval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				stopl = utopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
			if tipt == 'fh':
				tipval = fhvalt
				tip = fh
				i = tip
				tiptemp = fht
				if kji == 1:
					topl = fhtopl
					kl = 1
					kli = 1
					kp = 1
					kpi = 1
					kj = 1
					kji = 0
				fhtopl = topl
				tipol = fhval
				l = kolvo * tipol
				val = val - l
				topl = topl + kolvo
				fhtopl = utopl + kolvo
				print("у тебя осталось", val, "денег и", topl, "% топлива")
				minpl = 'l'
		if timet > 90:
			val = val + 300
			print("поздравляю! ты прошёл игру!")
			m =  input("Если хотите продолжить нажмите 'b' или любую другую клавишу чтобы закончить игру>>")
			if m == 'b':
				print("+ 300 денег, у вас", val, "денег")
				timet = timet - 91
			else:
				break
		if timet2 > 200:
			val = val + 1000
			print("поздравляю! ты прошёл эту фазу!")
			m =  input("Если хотите продолжить нажмите 'b' или любую другую клавишу чтобы закончить игру>>")
			if m == 'b':
				print("+ 1000 денег, у вас", val, "денег")
				timet = timet - 91
			else:
				break
		if topl < 1:
			print("вы проиграли, в реакторе не осталось топлива")
			break
		if temp > 1500:
			print(" ")
			print("              *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("   *         *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("   ***")
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("  *****")
			print("   ***")
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.1)
			print("*******")
			print("  *****")
			print("   ***")
			print("   ***     *")
			print("******   *")
			print("*************")
			print("*************")
			print(" ")
			time.sleep(0.5)
			print("вы проиграли, реактор взорвался")
			break
		if temp < 0:
			print("вы проиграли, реактор выключился")
			break
			