import random

r = random.randint(1, 100)

chance = 3
while chance > 0:
	user_guess = int(input('enter ur guess number: '))
	if user_guess == r:
		print ('猜對了你！')
		break
	else:
		if chance > 1:
			if user_guess > r:
				print ('再給你'+str(chance-1)+'次機會，順便提示：小一點。')
			else:
				print ('再給你'+str(chance-1)+'次機會，順便提示：大一點。')
		else:
			print ('再投一百元就多給三次機會。')
	chance -= 1