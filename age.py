# Legal age to drive 
driving = input('Have you driven any vehicle? (y/n): ')
if driving != 'y' and driving != 'n':
	print('You are only allowed to input either "y" or "n" for this question.')
	raise SystemExit
else: 
	age = input('How old are you now? ') 
	age = int(age)
	if driving == 'y':
		if age >= 18:
			print('You are qualified to drive.')
		else:
			print('Hey, why have you been allowed to driven?')
	else:
		if age >= 18:
			print('You are qualified to drive. Why do you not get your driver license?')
		else:
			print('Good. You can get your drive license after 18 years old.')