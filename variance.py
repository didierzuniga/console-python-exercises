# -*- coding: utf-8 -*-

import math

def run():
	n = int(input("¿Cuantos datos deseas ingresar? -> "))
	data = []
	sumData = 0
	sumresults = 0
	for x in range(n):
		inputs = int(input("Ingresa dato {}: ".format(x+1)))
		sumData += inputs
		data.insert(x,inputs)
	medium = sumData / len(data)
	for i in range(n):
		data[i] = data[i]-medium
	for j in range(n):
		sumresults += data[j]**2
		data[j] = data[j]**2
	print("La varianza es: {}".format(sumresults / len(data)))
	print("La desviación estándar es: {}".format(math.sqrt(sumresults / len(data))))

if __name__ == '__main__':
	run()