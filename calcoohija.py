#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Made by Felipe Sandoval Sibada

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):
	def multiply(self):
		return (self.var1 * self.var2)

	def divide(self):
		try:
			return (self.var1 / self.var2)
		except ZeroDivisionError:
			sys.exit("Division by zero is not allowed.")


if __name__ == "__main__":
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")
	except IndexError:
		sys.exit("Error: You need to give me numbers on the Command Line")

# making the object	
	variables = calcoo.Calculadora(operando1, operando2)

	if sys.argv[2] == "suma":
		result = CalculadoraHija.add(variables)
	elif sys.argv[2] == "resta":
		result = CalculadoraHija.minus(variables)
	elif sys.argv[2] == "multiplica":
		result = CalculadoraHija.multiply(variables)
	elif sys.argv[2] == "divide":
		result = CalculadoraHija.divide(variables)
	else:
		sys.exit('You can only add or subtract.')


	print(result)