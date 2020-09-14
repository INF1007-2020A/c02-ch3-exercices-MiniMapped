#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return 0

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	pass

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	sum = 0
	sum_values = 0
	for v in values:
		if v >= 0:
			sum += v
			sum_values += 1
	return (sum / sum_values)

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = tens = fives = twos = ones = 0
	while value != 0:
		if value >= 20:
			twenties = value//20
			value -= (twenties*20)
			pass
		elif value >= 10:
			tens = value // 10
			value -= (tens * 10)
			pass
		elif value >= 5:
			fives = value // 5
			value -= (fives * 5)
			pass
		elif value >= 1:
			twos = value // 2
			value -= (twos * 2)
			if value == 1:
				ones += 1
				value = 0
			pass

	return (twenties, tens, fives, twos, ones);

if __name__ == "__main__":
	#print(dissipated_power(69, 420))
	#print(orthogonal((1, 1), (-1, 1)))
	#print(average([1, 4, -2, 10]))
	print(bills(138))
